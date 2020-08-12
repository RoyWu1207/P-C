# coding:utf-8
import requests
# 失败的作品······
url = "https://www.luogu.com.cn/problem/solution/"
number = input("题目编号:")
url = url+number+"?page="+input("题解页数:")
try:
    responce = requests.get(url=url)
    print(responce.text)
finally:
    print("失败的作品,qo(╥﹏╥)o")
