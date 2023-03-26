# import requests
from requests import get

response = get("http://www.youtube.com/")

print(response.content)