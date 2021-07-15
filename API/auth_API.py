import requests
from utilities.configuration import get_password
from utilities.resourses import APIResources

# url_auth = 'https://github.com/login'
# github_response = requests.get(url_auth, auth=('rupeshmodak', get_password()))
# print(github_response.status_code)


se = requests.session()
se.auth = auth = ('rupeshmodak', get_password())
response = se.get(APIResources.github_url)
print(response.status_code)

