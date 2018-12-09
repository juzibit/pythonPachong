import requests
from bs4 import BeautifulSoup
import pandas as pd
url = 'http://www.runoob.com/html/html-intro.html'
response = requests.get(url)
html = response.text.encode(response.encoding).decode()
# print(html)
soup = BeautifulSoup(html, 'lxml')
l = [x.text for x in soup.findAll('h2')]
# print(l)
df = pd.DataFrame(l, columns=[url])
# link = soup.findAll('a')[1]
# link.has_attr('href')
# print(link)
# print(link.attrs['href'])
links = [i for i in soup.findAll('a')
         if i.has_attr('href') and i.attrs['href'][0:5] == '/html']
# print(links)
relative_urls = set([i.attrs['href'] for i in links])
# print(relative_urls)
# relative_urls.to_excel('url.xlsx')
absolute_urls = {'http://www.runoob.com' + i for i in relative_urls}
absolute_urls.discard(url)
# print(absolute_urls)

for i in absolute_urls:
    ri = requests.get(i)
    soupi = BeautifulSoup(ri.text.encode(ri.encoding), "lxml")
    li = [x.text for x in soupi.findAll('h2')]
    dfi = pd.DataFrame(li, columns=[i])
    df = df.join(dfi, how='outer')
# print(df)
df.to_excel('url.xlsx')

