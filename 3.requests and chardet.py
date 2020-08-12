# coding:utf-8
import requests,chardet
url = "https://www.50zww.net/"
response = requests.get(url=url)
print(response.text)
print(chardet.detect(response.content))
