from urllib import request
url = 'http://www.runoob.com/html/html-intro.html'
html = request.urlopen(url).read()
print(html.decode())
