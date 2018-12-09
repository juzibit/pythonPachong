import requests
from bs4 import BeautifulSoup
url = 'http://www.runoob.com/html/html-intro.html'
response = requests.get(url)
html = response.text.encode(response.encoding).decode()
soup = BeautifulSoup(html, 'lxml')
# print(soup)

# 使用标签
# print(soup.findAll(name={'h1','h2','h3','h4'}))
# print(len(soup.body.findAll('div',recursive = False)))

# 使用属性
divs = soup.findAll('div', attrs={'class': {'article', 'container navigation'}})
# print(divs)
print(divs[1].findAll('h2'))


