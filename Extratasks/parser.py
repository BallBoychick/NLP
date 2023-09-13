import json
import requests

params = {
    'text' : 'python',
    'area' : 1,
    'page' : 1,
    'only_with_salary': True
}
req = requests.get('https://api.hh.ru/vacancies', params=params)
data = req.content.decode()
obj = json.loads(data)
print(obj)
