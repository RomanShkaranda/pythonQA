from pprint import pprint
import requests
from tabulate import tabulate

url = "https://dummyjson.com/comments?limit=150"

response = requests.get(url)
response_json = response.json()
comments = response_json["comments"]

for comment in comments:
    if "awesome" in comment["body"].lower():
        print(comment["user"]["username"])




