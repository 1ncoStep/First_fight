
import json


with open('info.json', 'r', encoding='utf-8') as project:
    data = json.load(project)

print(data)