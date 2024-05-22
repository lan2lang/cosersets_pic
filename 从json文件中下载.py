import time
import json
import os
import aiohttp
import asyncio
from fake_useragent import UserAgent

# 异步下载文件函数
async def download_file(session, url, file_name, header):
    async with session.get(url, ssl=False, headers=header) as response:
        content = await response.read()
        with open(file_name, 'wb') as f:
            f.write(content)
        print(f"{file_name} 下载完成")

# 主异步函数，管理下载过程
async def main(url_list, download_dir):
    os.makedirs(download_dir, exist_ok=True)

    async with aiohttp.ClientSession(trust_env=True) as session:
        tasks = []
        ua = UserAgent()

        for file in url_list:
            header = {'User-Agent': ua.random}
            task = download_file(session, file['url'], os.path.join(download_dir, file['file_name']), header)
            tasks.append(task)

        await asyncio.gather(*tasks)
    print("所有下载任务完成！")

# 脚本的主要入口点
if __name__ == '__main__':
    # 获取用户标识库
    ua = UserAgent()

    # 避免aiohttp兼容性错误
    # asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    os.environ["http_proxy"] = "http://127.0.0.1:7890"
    os.environ["https_proxy"] = "http://127.0.0.1:7890"

    name = '叉子宝宝_388'
    json_dir = 'json/'

    download_dir = os.path.join('download', name)

    # 读取json文件
    with open(os.path.join(json_dir, f'{name}.json'), 'r', encoding='utf-8') as f:
        url_list = json.load(f)

    num_files = len(url_list)

    # 每次异步下载的数量
    batch_size = 60

    # 从第一张开始
    left = 0

    # 文件剩余下载数量
    while num_files > 0:
        right = left + batch_size
        current_batch = url_list[left:right]
        asyncio.run(main(current_batch, download_dir))

        time.sleep(8)  # 可选的休眠时间，避免触发速率限制

        left = right
        num_files -= batch_size

    if num_files > 0:
        print('进入if')
        current_batch = url_list[left:]
        asyncio.run(main(current_batch, download_dir))
