"""Number scraping assignment"""
import urllib.request
import urllib.parse
import urllib.error
import ssl
import re
from bs4 import BeautifulSoup

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter Url: ')
if len(url) <= 0:
    url = 'http://py4e-data.dr-chuck.net/comments_1919208.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('span')
count = 0
total = 0
for span in tags:
    num = re.findall('[0-9]+', span.decode())
    count += 1
    total += int(num[0])
print(f'Sum: {total}\nCount: {count}')
