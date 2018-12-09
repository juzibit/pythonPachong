import requests
from bs4 import BeautifulSoup
import pandas as pd
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0'}
cookies = {'cookie': 'lang=zh-cn; device=desktop; theme=default; keepLogin=on; windowWidth=1409; windowHeight=439; zentaosid=hgg8g8eh26gafa16kvns09vq07'}

url = 'http://pms.icil.net:8081/pro/company-dynamic-thisweek.html'
response = requests.get(url, cookies=cookies, headers=headers)
html = response.text.encode(response.encoding).decode()
print(html)
# with open('zentao.txt', 'wb+') as f:
#    f.write(response.content)
# print(response)
# html = response.text.encode(response.encoding).decode()
# soup = BeautifulSoup(html, 'lxml')
# l = [x.text for x in soup.findAll('td')]
# print(l)