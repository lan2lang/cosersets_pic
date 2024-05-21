import time

import json
import os
import aiohttp
import asyncio
from fake_useragent import UserAgent

header = {}


# 异步下载文件函数
async def download_file(session, url, file_name, header):
    async with session.get(url, ssl=False, headers=header) as response:
        content = await response.read()
        with open(file_name, 'wb') as f:
            f.write(content)
        print(f"{file_name} 下载完成")


async def main():
    # 下载文件存放目录
    download_dir = 'download/' + name + '/'
    os.makedirs(download_dir, exist_ok=True)

    # 创建异步会话
    async with aiohttp.ClientSession(trust_env=True) as session:
        tasks = []

        for file in url_list:
            header = {'User-Agent': ua.random}
            # print(header)

            # 创建下载任务
            task = download_file(session, file['url'], download_dir + file['file_name'], header)
            tasks.append(task)

        # 并发执行下载任务
        await asyncio.gather(*tasks)

    print("下载完成！")


# global urls

if __name__ == '__main__':
    ua = UserAgent()
    # 加上这一行,解决使用代理请求 https会报错问题
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    # #解决代理问题
    os.environ["http_proxy"] = "http://127.0.0.1:7890"
    os.environ["https_proxy"] = "http://127.0.0.1:7890"

    name = 'kaya萱_887'
    dir = 'json/'
    # url_list = []
    # 从json中读取链接
    with open(dir + name + '.json', 'r',encoding='utf-8') as f:
        url_list = json.load(f)

    # 控制一次下载的图片数量
    num = len(url_list)

    url_list_copy = url_list

    left=0
    right=100
    # url_list=url_list_copy[left:right]
    # # 运行异步主函数
    # asyncio.run(main())

    while num - 100 > 0:
        url_list=url_list_copy[left:right]
        # 运行异步主函数
        asyncio.run(main())
        time.sleep(10)
        num=num-100
        left=right
        right=right+100

    url_list=url_list_copy[left:num]
    asyncio.run(main())
