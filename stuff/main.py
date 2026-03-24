import json


with open('data.json', 'r') as file:

    json.load(file)

print(data)
print(type(data))