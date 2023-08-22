"""using import and sys"""
import requests
import sys

username = sys.argv[1]
token = sys.argv[2]

response = requests.get('https://api.github.com/user', auth=(username, token))
data = response.json()
print(data.get('id'))






