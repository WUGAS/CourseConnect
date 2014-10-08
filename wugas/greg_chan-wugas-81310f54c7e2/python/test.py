import json
array = '{"fruits": ["apple", "banana", "orange"]}'
data  = json.loads(array)
fruits_list = data['fruits']
print fruits_list
