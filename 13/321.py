import requests
# 请求
url="https://qa.yansl.com:8084/signup/post"
# res=requests.get(url,)# 返回消息实体
# print('响应头',res.headers)
# print(res.text)
# print(res.status_code)
# post请求带参数
import json
a={
  "phone": "1500569998",
  "pwd": "ska444",
  "rePwd": "ska444",
  "userName": "stsasx"
}
res=requests.post(url,data=a)
print('响应头',res.headers)
print(res.text,res.text)
# print(res.text,res.json)
print(res.status_code)
# html xml json-->text
# # print(res.text,type(res.text))-->json 会报错