import json

with open('main.json','r',encoding='utf-8')as f:
    print(json.loads(f.read()))
