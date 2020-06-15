# 負責request
import requests
import json
r = requests.get('http://127.0.0.1:3000/relation_vector')
print(r.status_code)  # 200成功
j = json.loads(r.content)  # str 轉乘json
print(j)
