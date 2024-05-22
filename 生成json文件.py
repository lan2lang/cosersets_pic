import os
import json
import requests

# 解决代理问题
os.environ["http_proxy"] = "http://127.0.0.1:7890"
os.environ["https_proxy"] = "http://127.0.0.1:7890"

def request_data(path):
    """
    发送请求获取数据

    Args:
        path (str): 文件路径

    Returns:
        list: 文件列表
    """
    try:
        r = requests.post(
            "https://www.cosersets.com/api/storage/files",
            data=(
                    '{"storageKey": "1", "path": "/' + path + '", "password": "", "orderBy": "name", "orderDirection": "asc"}'
            ).encode('utf-8'),
            headers={'Content-Type': 'application/json'}
        )

        return json.loads(r.text)['data']['files']

    except Exception as e:
        print(f"An error occurred while fetching data: {e}")
        return []

def get_urls(data):
    """
    获取文件链接

    Args:
        data (list): 文件列表

    Returns:
        list: 文件链接列表
    """
    url_list = []
    for item in data:
        url = item.get('url')

        # 如果没有地址
        if url is None:

            # 重新请求
            path = item['path'] + "/" + item['name']

            second_data = request_data(path)
            url_list.extend(get_urls(second_data))

        else:
            # 直到出现地址
            # 拼接文件名
            file_name = item['path'].replace("/", "_")[1:] + "_" + url.split("/")[-1]
            print(file_name)
            # 同时保存文件名和地址
            url_list.append({"file_name": file_name, "url": url})

    return url_list

def main():
    role_name = "Kitaro_绮太郎"  # 角色名

    # 请求数据
    data = request_data(role_name)

    # 从数据中获取链接
    url_list = get_urls(data)

    print(f"Total URLs found: {len(url_list)}")

    # 写入文件
    with open(f'./json/{role_name}_{len(url_list)}.json', 'w', encoding='utf-8') as f:
        json.dump(url_list, f)

if __name__ == "__main__":
    main()
