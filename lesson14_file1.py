import requests
from bs4 import BeautifulSoup
import re
url = 'http://www.runoob.com/html/html-intro.html'
response = requests.get(url)
html = response.text.encode(response.encoding).decode()
soup = BeautifulSoup(html, 'lxml')

# 使用正则表达式
# 查找标签名为h1至h9的tag
# print(soup.findAll(re.compile('h[1-9]')))

# 查找标签名为h1至h9， 且文本内容包括“HTML” 或“html”的tag
# print(soup.findAll(re.compile('h[1-9]'), text=re.compile(".*(HTML)|(html).*")))

# 查找地址为 //www 或 //http://www 开头的链接
print(soup.findAll('a', attrs={'href': re.compile("^//(www)|(http\:www).*")}))
print(soup.find('a', attrs={'href': re.compile("^//(www)|(http\:www).*")}))