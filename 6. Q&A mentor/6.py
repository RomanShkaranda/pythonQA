# pip - python install package - external library
# pip freeze > requirements.txt - what libs we should install
# pip

from pprint import pprint
import requests
import time

# url = "https://dummyjson.com/products/{page}"
#
# for id in range(1, 101):
#     response = requests.get(url.format(page=id))
#
#     print(response.json())

url = "https://dummyjson.com/products"

response = requests.get(url)
response_json = response.json()

products = response_json["products"]
pprint(products, width=120)

# while True:
#     total_cost = 0
#     for product in products:
#         # pprint(product, width=120)
#         total_cost += product["price"] * product["stock"]
#
#     print(total_cost)
#     time.sleep(10)

total_price = 0

for product in products:
    if product["rating"] > 4.5:
        total_price += product["price"] * product["stock"]

print(total_price)


