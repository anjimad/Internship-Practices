shopping_list=[]
def add_item(item):
    shopping_list.append(item)
    print(item,"added")
def remove_item(item):
    if item in shopping_list:
       shopping_list.remove(item)
       print(item,"removed")
    else:
        print("item not found.")
def show_list():
    print("Shopping_List:",shopping_list)
add_item("milk")
add_item("bread")
show_list()
remove_item("milk")
show_list()
import requests
response=requests.get("https://fakestoreapi.com/products?limit=5")
data=response.json()
for item in data:
    print(item["title"])