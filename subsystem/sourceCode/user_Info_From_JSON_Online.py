# user_Info_From_JSON_Online.py
# A script to parse GPS and user info from an online JSON file
# For Notre Dame EE Senior Design 2020 - VALET
# 	Author: Alden Kane

import wget
import json

target_url = 'http://seniordesign.ee.nd.edu/2020/Design%20Teams/valet/users.json'
fetched = wget.download(url=str(target_url))

data=fetched.read()
data=json.loads(fetched)

user_Street_Address = 
