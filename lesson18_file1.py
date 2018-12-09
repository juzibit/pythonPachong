import requests
from bs4 import BeautifulSoup
import re
import os
import pandas as pd
url = 'https://www.jianshu.com/p/1376959c3679'
# response = requests.get(url)
# html = response.text.encode(response.encoding).decode()
# soup = BeautifulSoup(html, 'lxml')
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0'}
r = requests.get(url, headers=headers)
html = r.text.encode(r.encoding).decode()
# print(html)
soup = BeautifulSoup(html, 'lxml')
imgs = soup.findAll(lambda tag: tag.name == 'img' and tag.has_attr('data-original-src'))
# print(imgs)
srcs = [i.attrs['data-original-src'] for i in imgs]
# print(srcs)
sources = ['https:'+src for src in srcs]
for i in sources:
    print(i)

filedir = os.getcwd()+'/picture'
if not os.path.exists(filedir):
    os.mkdir(filedir)
for i in range(len(sources)):
    rpi = requests.get(sources[i], headers = headers)
    if rpi.status_code == 200:
        with open(filedir + '/%s.jpg' % i, mode='wb') as f:
            f.write(rpi.content)
            print('downloading %d picture' %i)