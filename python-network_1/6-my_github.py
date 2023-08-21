"""using import and sys"""
import requests
import sys

username = sys.argv[1]
password = sys.argv[2]

response = requests.get(f"https://api.github.com/users/", auth=(username, password))
user_data = response.json() if response.status_code == 200 else None
print(user_data.get('id', 'None'))


