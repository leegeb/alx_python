"""script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter"""
import requests
import sys

if len(sys.argv) > 1:
    letter = sys.argv[1]
else:
    letter = ""

url = "http://0.0.0.0:5000/search_user"
data = {'q': letter}

response = requests.post(url, data=data)

try:
    json_data = response.json()
    if json_data:
        print("[{}] {}".format(json_data.get('id'), json_data.get('name')))
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")
