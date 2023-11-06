"""XML assignment"""
import urllib.request
import urllib.parse
import urllib.error
import ssl
import xml.etree.ElementTree as ET

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')
if url == '':
    url = 'http://py4e-data.dr-chuck.net/comments_1919210.xml'

xml = urllib.request.urlopen(url, context=ctx).read()

tree = ET.fromstring(xml)
comments = tree.findall('comments/comment')
print(f'Retrieving {url}')
print(f'Count: {len(comments)}')

total = 0
for comment in comments:
    total += int(comment.find('count').text)
print(f'Sum: {total}')
