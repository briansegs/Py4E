"""Extracting data from json assignment"""
import urllib.request
import urllib.parse
import urllib.error
import json

url = input('Enter url: ')
if url == '':
    url = 'http://py4e-data.dr-chuck.net/comments_1919211.json'

print(f'Retrieving: {url}')
raw = urllib.request.urlopen(url)
data = raw.read().decode()

js = json.loads(data)

total = 0
for item in js['comments']:
    total += item['count']
print(f'Sum:  {total}')
