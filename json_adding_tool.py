import json
import sys

with open('ProcessedData/data.json', 'w') as json_file:
    data = json.load(json_file, indent=4) 

print(data)