# user_Info_From_JSON_Online.py
# A script to parse GPS and user info from an online JSON file
# For Notre Dame EE Senior Design 2020 - VALET
# 	Author: Alden Kane

import urllib
import requests

target_url = 'http://seniordesign.ee.nd.edu/2020/Design%20Teams/valet/users.json'

try:
    urllib.request.urlopen(target_url)
    print("Accessed URL!")
except:
    exit()

# Fetch JSON Using Requests
data = requests.get(target_url).json()

firstName = data["firstName"]
lastName = data["lastName"]
userKey = data["userKey"]
lat = data["latitude"]
long = data["longitude"]

print(lat)
print(long)


