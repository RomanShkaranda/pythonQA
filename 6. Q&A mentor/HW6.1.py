# завдання 1
#
# урл http://api.open-notify.org/astros.json
# вивести список всіх астронавтів, що перебувають в даний момент на орбіті (дані не фейкові, оновлюються в режимі реального часу)


import requests
astr_list = []

url = "http://api.open-notify.org/astros.json"
response = requests.get(url)
response_json = response.json()

for astr in response_json["people"]:
    astr_list.append(astr["name"])

print(astr_list)
print(response_json)



