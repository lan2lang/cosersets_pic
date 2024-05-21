import time

from selenium import webdriver
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# 设置浏览器驱动路径
driver_path = 'msedgedriver.exe'  # 根据你的实际路径修改
browser = webdriver.Chrome()

# 目标网站的URL
url = 'https://www.cosersets.com/1/main/%E5%91%A8%E5%8F%BD%E6%98%AF%E5%8F%AF%E7%88%B1%E5%85%94%E5%85%94/%E9%98%BF%E5%8F%94%E7%89%B9%E7%9A%AE-%E6%97%97%E8%A2%8D'

# 打开网站
browser.get(url)

# 这里可以根据需要进行登录等操作

time.sleep(3)

# 获取页面内容
html = browser.page_source

# #解决代理问题
os.environ["http_proxy"] = "http://127.0.0.1:7890"
os.environ["https_proxy"] = "http://127.0.0.1:7890"

# 使用BeautifulSoup解析页面内容
soup = BeautifulSoup(html, 'html.parser')

#
dir = 'images/5/'
# 创建保存图片的目录
os.makedirs(dir, exist_ok=True)

# 关闭浏览器
browser.quit()

try:
    # 获取所有图片元素
    img_tags = soup.find_all('img')

    # 遍历图片元素并下载图片
    for img_tag in img_tags:
        # 获取图片的src属性
        img_url = img_tag.get('src')
        print(img_url)

        # 使用urljoin构建完整的图片URL
        # img_url = urljoin(url, img_url)

        # 获取图片内容
        img_data = requests.get(img_url).content

        # 提取图片文件名
        img_name = os.path.join(dir, os.path.basename(img_url))

        # 保存图片
        with open(img_name, 'wb') as img_file:
            img_file.write(img_data)
except:
    print('出现错误')
