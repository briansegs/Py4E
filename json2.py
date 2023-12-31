""""JSON practice 2"""
import json

inputs = """
[
    {
        "id" : "001",
        "x" : "2",
        "name" : "Chuck"
    },{
        "id" : "009",
        "x" : "7",
        "name" : "Berry"
    }
]
"""

info = json.loads(inputs)
print(f'User count: {len(info)}\n')

for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])
