# coding:utf-8
import requests
from bs4 import BeautifulSoup
url = "https://python123.io/ws/demo.html"
response = requests.get(url, timeout=30)
response.encoding = response.apparent_encoding
html = response.text
soup = BeautifulSoup(html, "html.parser")
soup.find_all("a")
soup.body.contents
soup.prettify()
