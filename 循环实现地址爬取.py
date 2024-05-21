import os

import json

import requests

# #解决代理问题
os.environ["http_proxy"] = "http://127.0.0.1:7890"
os.environ["https_proxy"] = "http://127.0.0.1:7890"


def request_data(path):
    r = requests.post(
        "https://www.cosersets.com/api/storage/files",
        data=(
                '{"storageKey": "1", "path": "/' + path + '", "password": "", "orderBy": "name", "orderDirection": "asc"}'
        ).encode('utf-8'),
        headers={'Content-Type': 'application/json'}
    )

    return json.loads(r.text)['data']['files']


role_name = "阿包也是兔娘"  # 角色名
file_name = ''
url_list = []

data = request_data(role_name)


def appent_to_list():
    pass


def get_urls():
    # 对第一层目录遍历
    for i in data:
        url = i['url']
        if url is None:
            # 继续请求
            path = i['path'] + "/" + i['name']
            print(path)
            second_data = request_data(path)
            # 对第二层目录遍历
            for j in second_data:
                url = j['url']
                if url is None:
                    path = j['path'] + "/" + j['name']
                    print(path)
                    third_data = request_data(path)
                    # print(third_data)
                    # 对第三层目录遍历
                    for k in third_data:
                        url = k['url']
                        if url is None:
                            print('地址为空')
                        else:
                            file_name = path.replace("/", "_")[1:] + "_" + url.split("/")[-1]
                            print(file_name)
                            print(url)
                            dict = {"file_name": file_name, "url": url}
                            url_list.append(dict)
                else:
                    file_name = path.replace("/", "_")[1:] + "_" + url.split("/")[-1]
                    print(file_name)
                    print(url)
                    dict = {"file_name": file_name, "url": url}
                    url_list.append(dict)
        else:
            pass
            # url_list.append(url)


get_urls()
print(len(url_list))
# 将字典保存到json
with open('./json/' + role_name + "_" + str(len(url_list)) + '.json', 'w', encoding='utf-8') as f:
    json.dump(url_list, f)
