"""using import and sys"""
import requests
import sys

username = sys.argv[1]
token = sys.argv[2]

response = requests.get(f"https://api.github.com/users/{username}", auth=(username, token))

if response.status_code == 200:
    user_data = response.json()
    print(user_data.get('id'))
else:
    print("None")





