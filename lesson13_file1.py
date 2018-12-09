import requests
from bs4 import BeautifulSoup
import re
url = 'http://www.runoob.com/html/html-intro.html'
response = requests.get(url)
html = response.text.encode(response.encoding).decode()
soup = BeautifulSoup(html, 'lxml')

# 使用lambda表达式
# print(soup.findAll(lambda tag: tag.name == 'h2' and len(tag.attrs) == 0))
# print(soup.findAll(lambda tag: tag.name == 'h2'))

# print([x for x in soup.findAll('h2') if len(x.attrs) == 0])

print(list(filter(lambda tag: len(tag.attrs) == 0, soup.findAll('h2'))))
