"""XML practice 2"""
import xml.etree.ElementTree as ET

data = """
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>
"""

stuff = ET.fromstring(data)
lst = stuff.findall('users/user')
print(f'User count: {len(lst)} \n')

for item in lst:
    print('Name:', item.find('name').text)
    print('Id:', item.find('id').text)
    print(f'Attribute: {item.get("x")} \n')
