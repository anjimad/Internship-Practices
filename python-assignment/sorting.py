import requests
url="https://fakestoreapi.com/products?limit=5"
response = requests.get(url)
products = response.json()
sorted_product = sorted(products,key=lambda x:x['rating']['rate'],reverse=True)
for product in sorted_product:
    print("Title:",product['title'])
    print("Rating:",product['rating']['rate'])
    print("-" * 40)