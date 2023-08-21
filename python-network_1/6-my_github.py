"""my github"""
import requests
import sys
import os

username = sys.argv[1]
token = os.environ.get("GITHUB_TOKEN")

url = f"https://api.github.com/users/{username}"

response = requests.get(url, auth=(username, token))

if response.status_code == 200:
    user_data = response.json()
    print(f"GitHub ID: {user_data['id']}")
else:
    print(f"Error: {response.status_code}")
