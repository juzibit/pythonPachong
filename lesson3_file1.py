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
print(df)
# df.to_excel('pachong.xlsx')
# df.iloc[2,0]
