from pprint import pprint
import requests
from tabulate import tabulate

url = "https://dummyjson.com/todos?limit=150"

response = requests.get(url)
response_json = response.json()
todos = response_json["todos"]

# pprint(response_json["todos"], width=120)

# print(tabulate(todos, headers="keys", tablefmt="grid"))

for todo in todos:
    if todo["userId"] == 48 and todo["completed"] is False:
        print(todo["todo"])


