# coding:utf-8
from urllib import request
url = "http://www.baidu.com/"
response = request.urlopen(url)
data = response.read()
print(data.decode("utf-8"))
