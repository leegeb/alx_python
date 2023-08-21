"""script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header"""
"""importing requests"""

"""importing sys"""

import requests
import sys
url = sys.argv[1]


request = requests.get(url)
try:
    print(request.headers['X-Request-Id'])
except:
    pass
