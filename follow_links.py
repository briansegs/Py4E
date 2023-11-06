"""Follow links assignment"""
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
if url == '':
    url = 'http://py4e-data.dr-chuck.net/known_by_Harikrishna.html'

position = input('Enter position: ')
if position == '':
    position = 18
else:
    position = int(position)

count = input('Enter count: ')
if count == '':
    count = 7
else:
    count = int(count)

pos = position
while count != 0:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    print(f'Retrieving: {url}')

    links = soup('a')
    for link in links:
        if pos == 0:
            count -= 1
            pos = position
            break
        pos -= 1
        nxt = re.findall('"(.*)"', link.decode())
        url = nxt[0]

print(f'Retrieving: {url}')
name = re.findall('by_(.*).html', url)
print(f'The answer is {name[0]}')
