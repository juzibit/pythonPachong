import requests
from bs4 import BeautifulSoup
url = 'http://www.runoob.com/html/html-intro.html'
response = requests.get(url)
html = response.text.encode(response.encoding).decode()
# print(html)
soup = BeautifulSoup(html, 'lxml')
# print(soup)
# print(soup.head)
# print(soup.body)
# print(soup.body.div.div)
# print(soup.h1, soup.h2)
# print(soup.findAll('h2'))

