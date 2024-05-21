import os
import requests
from fake_useragent import UserAgent

import json

from tqdm import tqdm

# #解决代理问题
os.environ["http_proxy"] = "http://127.0.0.1:7890"
os.environ["https_proxy"] = "http://127.0.0.1:7890"

# 保存目录
dir = 'download/瓜希酱_670/'


def download_from_json(file_name):
    # 读取JSON文件中的数据
    with open(file_name, 'r', encoding='utf-8') as f:
        url_list = json.load(f)
        # count = 1
    for file in url_list:
        # 逐一下载
        # 用户标识
        ua = UserAgent()
        header = {'User-Agent': ua.random}
        # print(header)
        # 创建目录
        os.makedirs(dir, exist_ok=True)
        # 请求
        content = requests.get(file['url'], headers=header).content
        # 写入
        with open(dir + file['file_name'], 'wb') as f:
            print(file['file_name'])
            f.write(content)
        # count += 1
    print(f"下载完成")


if __name__ == "__main__":
    # 调用下载函数
    download_from_json('json/瓜希酱_670.json')
