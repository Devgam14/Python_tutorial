import faker 
import requests as req
url = "https://api.github.com"
response = req.get(url)
print(response.status_code)
print(response.text)

