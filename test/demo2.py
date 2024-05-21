# import requests
# import json
# import os
#
# #解决代理问题
# os.environ["http_proxy"] = "http://127.0.0.1:7890"
# os.environ["https_proxy"] = "http://127.0.0.1:7890"
#
# # proxy = {'http': "127.0.0.1:7890",
# #          'https': "127.0.0.1:7890"}
#
# # r = requests.get(
# #     "https://www.cosersets.com/api/list/1?path=%2FFushii_%E6%B5%B7%E5%A0%82%2F%E8%BF%91%E8%B7%9D%E7%A6%BB%E6%81%8B%E7%88%B1&password=&orderBy=&orderDirection=",
# #     proxies=proxy)
# #
# # with open('img.json', 'w',encoding=r.encoding) as f:
# #     f.write(r.text)
#
# with open('img.json', 'rb') as f:
#     data = json.load(f)
#
# file_url = data['data']['files'][0]['url']
# dirName = f"{file_url.split('/')[-3]}/{file_url.split('/')[-2]}"
#
# # os.makedirs(dirName)
#
# for i in data['data']['files']:
#
#     url=i['url']
#     img_data = requests.get(url).content
#     fname=url.split('/')[-1]
#
#     file_url = os.path.join(dirName, fname)
#
#     with open(file_url, 'wb') as f:
#         f.write(img_data)
#
#
