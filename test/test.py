import json
import re
from urllib.parse import quote_plus

str='https://zfile.cosersets.com/file/1/Byoru/DoA Venus Bikini by Hidori Rose & Byoru/001.webp'
# pattern = r'https.*?\.webp'
#
# # 进行匹配
# match = re.search(pattern, str)
# result = match.group()
# print(result)
# 进行URL编码
with open('all-son.json', 'r') as f:
    names = json.load(f)
list=[]
for name in names:
    list.append(quote_plus(name))

# 保存到json
with open('all-son3.json', 'w', encoding='utf-8') as f:
    json.dump(list, f)
