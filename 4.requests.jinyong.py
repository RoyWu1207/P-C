# conding:utf-8
import requests
response = requests.get("http://www.jinyongwang.com/shen/781.html")
response.encoding = "utf-8"
print(response.text)
url = "http://www.jinyongwang.com/shen/781.html"
response = requests.get(url, timeout=30)
type(response)
print(response.text[:500])
print(response.status_code)
