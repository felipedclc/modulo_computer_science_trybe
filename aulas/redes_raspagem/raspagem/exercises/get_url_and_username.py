import requests

# from parsel import Selector

response = requests.get("https://api.github.com/users")
json_response = response.json()
# print(json_response)
# print([f"{user['login']} {user['url']}" for user in json_response])

for user in json_response:
    print(f"{user['login']} {user['url']}")
