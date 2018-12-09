import requests
from bs4 import BeautifulSoup
import re
import os
import pandas as pd
url = 'http://www.runoob.com/html/html-intro.html'
response = requests.get(url)
html = response.text.encode(response.encoding).decode()
soup = BeautifulSoup(html, 'lxml')

# print(len(list(soup.body.children)))
# print(len(list(soup.body.descendants)))
# print(list(soup.body.find('div').next_siblings))
# print(len(list(soup.body.find('div').next_siblings)))
print(soup.body.find('div').parent.name)
