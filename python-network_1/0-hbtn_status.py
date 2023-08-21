# importing requests
import requests
# Defining the URL to fetch data from
url = 'https://alu-intranet.hbtn.io/status'

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print("Body response:")
    print("\t- type: {}".format(type(data)))
    print("\t- content: {}".format(data))
else:
    print("Error: Unable to fetch data from the URL. Status code: {}".format(
        response.status_code))
