# import random
# import time
import requests

# from lxml import etree
# import xlwt

# url = 'http://m.hlxns.com/m/?r=l&u=427272'
# url = 'https://blog.csdn.net/programmer_yf/article/details/80697290'
url = 'http://www.runoob.com/html/html-intro.html'
response = requests.get(url)
# response.encode = 'utf-8'
# print(response.text)
# print(response.text.encode(response.encoding).decode())
html = response.text.encode(response.encoding).decode()
# print(html)
print(html[0:1000])
