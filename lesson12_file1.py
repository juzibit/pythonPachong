import requests
from bs4 import BeautifulSoup
import re
url = 'http://www.runoob.com/html/html-intro.html'
response = requests.get(url)
html = response.text.encode(response.encoding).decode()
soup = BeautifulSoup(html, 'lxml')

# 使用文本
# 查看文本内容为‘HTML 标签’的所有html元素（tag对象）
# print(soup.findAll(name = re.compile(''), text='HTML 标签'))

# 查看文本内容以‘HTML'开头的tag对象
# print(soup.findAll(re.compile(''), text=re.compile('^HTML')))
# 查看文本内容以‘HTML'开头的tag对象, 限制为标题类tag
# print(soup.findAll({'h1', 'h2', 'h3', 'h4'}, text=re.compile('^HTML')))

# 使用关键字
# 因为class是Python关键字，此处有要用class指定属性名，为避免冲突，需要加下划线
# print(soup.findAll(class_={'article', 'container navigation'}))

# 关键字参数**warg 和 attrs参数，可以互相替代
print(soup.findAll('div', id={'footer'}))





