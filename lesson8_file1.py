import requests
from bs4 import BeautifulSoup
r = requests.get('https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%C8%D9%D2%AB%BD%F8%D0%D0%CA%B1&fr=ala&ala=1&alatpl=adress&pos=0&hs=2&xthttps=111111')
soup = BeautifulSoup(r.text.encode(r.encoding), 'lxml')

