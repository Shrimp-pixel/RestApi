import requests
from requests.auth import HTTPBasicAuth

#auth = HTTPBasicAuth(username='admin', password='admin')

#response = requests.get('http://127.0.0.1:8000/api/todo/', auth=auth)
#print(response.status_code)
#print(response.json())





#payload = {'username': 'admin', 'password':'admin'}
#response = requests.post('http://127.0.0.1:8000/api-token-auth/', data=payload)
#
#print(response.status_code) #{'token': 'acf1f010eb49c9aa672d88f4ed8be49ce24ac821'}
#print(response.json()) #{'token': 'acf1f010eb49c9aa672d88f4ed8be49ce24ac821'}

headers = {'Authorization': 'acf1f010eb49c9aa672d88f4ed8be49ce24ac821'}
response = requests.get('http://127.0.0.1:8000/api/todo/', headers=headers)

print(response.status_code)
print(response.json())
