"""my github"""
import requests
import sys
import os

username = sys.argv[1]
token = os.environ.get("GITHUB_TOKEN")

response = requests.get(f"https://api.github.com/users/{username}", auth=(username, token))

print(response.json().get('id', 'Error'))
