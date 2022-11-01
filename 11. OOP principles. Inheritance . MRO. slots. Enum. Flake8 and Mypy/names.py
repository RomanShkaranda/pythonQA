import requests
import random

url = 'https://dummyjson.com/users?limit=10'
response = requests.get(url)
users = response.json()['users']

names = []
last_names = []

for i in users:
    names.append(i['firstName'])

for i in users:
    last_names.append(i['lastName'])


name = random.choice(names)
last_name = random.choice(last_names)
salary = random.randrange(10000, 50000)



