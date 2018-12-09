import requests
from bs4 import BeautifulSoup
import re
import os
import pandas as pd
url = 'http://www.shicimingju.com/chaxun/list/3710.html'
response = requests.get(url)
html = response.text.encode(response.encoding).decode()
soup = BeautifulSoup(html, 'lxml')

content = soup.find('div', class_='shici-content').text

# 数据清洗
content = re.sub('(\r\n\xa0)', '', content)
# print(content)
content = re.sub('\(.*\)', '', content)
# print(content)
content = re.sub('\(.*?\)', '', content)  # 懒惰匹配.*?
# print(content)
title = soup.find('div', class_='shici-content').parent.h1.text
# print(title)
'存储到txt文档'
filedir = os.getcwd() + '/sushideci'
if not os.path.exists(filedir):
    os.mkdir(filedir)
with open(filedir + '/%s.txt'%title, mode='w', encoding='utf-8') as f:
    f.write(title + '\n' + content)
