"""importing requests"""
import requests
"""Defining the URL to fetch data from"""
url = 'https://alu-intranet.hbtn.io/status'

request = requests.get(url)
print("Body response:")
print("\t- type:", type(request.reason))
print("\t- content:", request.reason)
