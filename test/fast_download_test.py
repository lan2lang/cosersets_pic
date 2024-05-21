import asyncio
import os
import threading
import time

import aiohttp
import requests
import json

from tqdm import tqdm

# #解决代理问题
os.environ["http_proxy"] = "http://127.0.0.1:7890"
os.environ["https_proxy"] = "http://127.0.0.1:7890"

api = 'https://www.cosersets.com/api/list/1?path=/'

skip_key = {}

name = '你的负卿'


# 异步下载文件函数
async def download_file(session, url, file_name):
    async with session.get(url) as response:
        content = await response.read()  # 请求数据

        with open(file_name, 'wb') as f:  # 写入文件
            f.write(content)

        print(f"{file_name} 下载完成")


async def download_from_json(data):
    """
        备份
    :param data:
    :return:
    """
    # 获取第一个文件的URL
    global file_url

    for i in data['data']['files']:
        file_url = i['url']

        if file_url is not None:
            break

    # 根据URL构建目录名
    dir_name = f"{file_url.split('/')[-3]}/{file_url.split('/')[-2]}"

    # 创建目录，如果目录已存在则忽略
    os.makedirs(dir_name, exist_ok=True)

    print(dir_name)

    # 创建异步会话
    async with aiohttp.ClientSession() as session:

        tasks = []
        # 遍历所有文件数据
        for item in data['data']['files']:
            url = item['url']
            if url is None:
                print('已跳过' + item['name'])
                continue

            file_name = url.split('/')[-1]
            file_name = os.path.join(dir_name, file_name)
            # 添加协程任务
            task = download_file(session, url, file_name)
            tasks.append(task)

        # 并发执行下载任务
        await asyncio.gather(*tasks)


# 根据人名请求api
r = requests.get(api + name)
contain_dir_json = r.text

r.close()

# 解析返回的json
data = json.loads(contain_dir_json)['data']['files']

count = 0
t_list = []
# 再次循环请求具体地址
for i in data:
    # if count < 2:  # 2代表跳过前两个
    #     print(f'已跳过{i["name"]}')
    #     count = count + 1
    #     continue
    flag = True
    for key in skip_key:
        if key in i['name']:
            print(f'已跳过{i["name"]}')
            flag = False
            break

    if not flag:
        continue

    # 拼接请求地址
    address = api + name + '/' + i['name']

    r = requests.get(address)
    # 请求
    pic_address_json = r.text

    r.close()
    # 解析json
    info = json.loads(pic_address_json)

    # 下载图片
    # 运行异步主函数
    asyncio.run(download_from_json(info))

    time.sleep(5)
# for t in t_list:
#     t.join()
# 解析json获取到下载地址，下载图片
