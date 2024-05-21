import os
import re
import threading
import time

import requests
import json

from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from selenium import webdriver
from tqdm import tqdm

# #解决代理问题
os.environ["http_proxy"] = "http://127.0.0.1:7890"
os.environ["https_proxy"] = "http://127.0.0.1:7890"

api = 'https://www.cosersets.com/1/main'

os.makedirs('All', exist_ok=True)
# 用户标识
ua = UserAgent()
header = {'User-Agent': ua.random}


def init():
    '''
    初始化
    :return:
    '''
    # 设置浏览器驱动路径
    driver_path = 'msedgedriver.exe'  # 根据你的实际路径修改
    browser = webdriver.Chrome()

    # 打开浏览器
    # 打开网站
    browser.get(api)

    # 这里可以根据需要进行登录等操作

    time.sleep(3)

    # 获取页面内容
    html = browser.page_source

    browser.quit()

    soup = BeautifulSoup(html, 'html.parser')

    # 使用class选择器获取class为'cell'的元素
    cell_element = soup.findAll('div', class_='cell')

    list = []
    for i in cell_element:
        list.append(i.text.strip())

    # 保存到json
    with open('all.json', 'w', encoding='utf-8') as f:
        json.dump(list, f)
    # 关闭浏览器


api = 'https://www.cosersets.com/api/list/1?path=/'


def get_son_dir():
    """
    获取到子目录
    :return:
    """
    # 从json中读取名字
    with open('all.json', 'r') as f:
        names = json.load(f)
    list = []
    for name in names:
        # 生成链接
        # 根据人名请求api
        r = requests.get(api + name)
        contain_dir_json = r.text
        r.close()

        # print(contain_dir_json)
        # 解析返回的json
        data = json.loads(contain_dir_json)['data']['files']

        try:
            print(name + '/' + data[1]['name'])
            list.append(name + '/' + data[1]['name'])
        except:
            print(name + '/' + data[0]['name'])
            list.append(name + '/' + data[0]['name'])

    # 保存到json
    with open('all-son.json', 'w', encoding='utf-8') as f:
        json.dump(list, f)


# 请求子目录，保留第一张照片
# 从json中读取名字
with open('all-son3.json', 'r') as f:
    names = json.load(f)
list = []
# 定义正则表达式模式
pattern = r'https.*?\.webp'
for name in names:
    # 生成链接
    # 根据人名请求api
    r = requests.get(api + name)
    str = r.text
    # print(str)
    r.close()

    # 进行匹配
    match = re.search(pattern, str)
    if not match is None:
        result = match.group()
        print(result)
        list.append(result)
    else:
        print(name)
# 保存到json
with open('../json/all-pic.json', 'w', encoding='utf-8') as f:
    json.dump(list, f)
