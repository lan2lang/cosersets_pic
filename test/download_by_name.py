import os
import threading
import time
import traceback

import requests
import json

from tqdm import tqdm

# #解决代理问题
os.environ["http_proxy"] = "http://127.0.0.1:7890"
os.environ["https_proxy"] = "http://127.0.0.1:7890"

api = 'https://www.cosersets.com/api/list/1?path=/'

skip_key = {}

name = '森萝财团/X-022'


def download_from_json(data):
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

    if file_url is None:
        print('返回')
        return

    print(data['data']['files'])

    file_url=data['data']['files'][1]['url']

        # 根据URL构建目录名
    dir_name = f"{file_url.split('/')[-3]}/{file_url.split('/')[-2]}"

    # 创建目录，如果目录已存在则忽略
    os.makedirs(dir_name, exist_ok=True)

    print(dir_name)

    # 遍历所有文件数据
    for item in data['data']['files']:
        url = item['url']

        if url is None:
            print('已跳过' + item['name'])
            continue

        with requests.get(url) as r:
            img_data = r.content
            fname = url.split('/')[-1]

            # 构建文件的完整路径
            file_path = os.path.join(dir_name, fname)

            # 将图片数据写入文件
            with open(file_path, 'wb') as f:
                f.write(img_data)

        # time.sleep(0.1)


try:
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
        if count < 1:  # 2代表跳过前两个
            print(f'已跳过{i["name"]}')
            count = count + 1
            continue
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

        # t = threading.Thread(target=download_from_json(info), args=())
        # t_list.append(t)
        # t.start()

        # count = count + 1
        # print(info)
        # 下载图片
        download_from_json(info)
        # time.sleep(0.1)

except Exception as e:
    # traceback.print_exc()
    print(e)
# for t in t_list:
#     t.join()
# 解析json获取到下载地址，下载图片
