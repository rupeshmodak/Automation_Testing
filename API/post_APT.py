import requests

from payLoad import *
from utilities.configuration import *
from utilities.resourses import APIResources

headers = {"Content-Type": "application/json;charset=UTF-8"}
url_add = get_config()['API']['endpoint'] + APIResources.addBook
url_delete = get_config()['API']['endpoint'] + APIResources.deleteBook

response_add = requests.post(url_add, json=addbook_payload(9876), headers=headers,)
addbook = response_add.json()
print(addbook)
print(type(addbook))
print(addbook['ID'])
bookID = addbook['ID']

print("______________________________")

response_del = requests.post(url_delete, json={"ID": bookID}, headers=headers,)
deletebook = response_del.json()
print(deletebook)
assert deletebook['msg'] == 'book is successfully deleted'

print("_______________________________")

query = "select * from Books"
response_addBook = requests.post(url_add, json=payload_DB(query), headers=headers,)
addnewbook = response_addBook.json()
print(type(addnewbook))









