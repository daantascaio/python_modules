# requests para requisições HTTP
# Tutorial -> https://youtu.be/Qd8JT0bnJGs
import requests

# http:// -> port: 80
# https:// -> port: 443
url = 'http://localhost:3333/'
response = requests.get(url)

# print(response)

print(response.status_code)
# print(response.headers)
# print(response.content)
print(response.text)
# print(response.json())
