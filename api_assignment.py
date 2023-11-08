""""json api assignment"""
import urllib.request
import urllib.parse
import urllib.error
import json

service_url = 'http://py4e-data.dr-chuck.net/json?'

address = input('Enter location: ')
if address == '':
    address = 'Oregon Institute of Technology'

url = service_url + urllib.parse.urlencode({'key': 42, 'address':address})

print(f'Retreving: {url}')
uh = urllib.request.urlopen(url)
data = uh.read().decode()

try:
    js = json.loads(data)
except:
    js = None

if not js or 'status' not in js or js['status'] != 'OK':
    print('==== Failure to Retrieve ====')
    print(data)

print(f'Place id: {js["results"][0]["place_id"]}')
