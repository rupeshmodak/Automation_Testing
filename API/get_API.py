import requests
import json

response = requests.get('http://216.10.245.166/Library/GetBook.php',
                        params={'AuthorName': 'Rupesh Modak'},)
print(response.text)
print(type(response.text))
str_response = json.loads(response.text)
print(str_response)
print(type(str_response))
print(str_response[0]['isbn'])

print("___________________________________________")

json_response = response.json()
print(json_response)
print(type(json_response))
print(json_response[0]['isbn'])

print("___________________________________________")

print(response.status_code)
print(response.headers)

print("___________________________________________")

for actulbook in json_response:
    if actulbook['isbn'] == 'zyx':
        print(actulbook)
        break
expectedbook = {"book_name":"Learn Python","isbn":"zyx","aisle":"888"}
assert actulbook == expectedbook







