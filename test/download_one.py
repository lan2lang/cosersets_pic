import requests
from bs4 import BeautifulSoup
import os
import time
import imghdr

url='https://www.cosersets.com/1/main/%E7%A5%9E%E6%A5%BD%E5%9D%82%E7%9C%9F%E5%86%AC/%E7%9C%9F%E5%86%AC%E3%81%AE%E7%94%B5%E5%AD%90%E7%9B%B8%E5%86%8C1.%E3%80%8A%E9%AD%94%E6%B3%95%E3%82%92%E4%BD%BF%E3%81%88%E3%81%AA%E3%81%84%E3%81%AE%E6%97%A5%E5%B8%B8%E3%80%8B'
# 获取网页内容
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')

print(resp.text)
# 获取图片URL列表
img_urls = []

# imgType_list = {'jpg', 'bmp', 'png', 'jpeg', 'rgb', 'tif'}


for img in soup.find_all('img'):
    img_url = img.get('src')
    img_urls.append(img_url)

print(img_urls)