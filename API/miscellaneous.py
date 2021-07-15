import requests

from utilities.configuration import get_password

se = requests.session()

se.auth = auth = ('rupeshmodak', get_password())
url_1 = "https://api.github.com/user/repos"
response_github = se.get(url_1)
print(response_github.status_code)
print(response_github.text)


print("___________________________________")

se.cookies.update({'visit-month': 'June'})
cookie = {'visit-year': '2021'}
response = se.get("https://httpbin.org/cookies", cookies=cookie)
print(response.status_code)
print(response.text)

print("______________________________")
response_1 = requests.get("http://rahulshettyacademy.com", allow_redirects=False, timeout=1)
# print(response_1.history)
print(response_1.status_code)

print("______________________________")
url_2 = "https://petstore.swagger.io/v2/pet/9843217/uploadImage"
file = {'file': open('C:\\Users\\Aparna\\Desktop\\11A.jpg', 'rb')}
response_2 = requests.post(url_2, files=file)
print(response_2.status_code)
print(response_2.text)
