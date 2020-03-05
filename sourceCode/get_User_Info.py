# user_Info_From_JSON_Online.py
# A script to parse GPS and user info from an online JSON file
# For Notre Dame EE Senior Design 2020 - VALET
# 	Author: Alden Kane

import urllib
import requests

def get_User_Info(target):
    # Declare Target URL for User Info
    target_url = target

    # Ensure We Can Access URL, Error Handling
    try:
        urllib.request.urlopen(target_url)
    except:
        exit()

    # Fetch JSON Using Requests
    data = requests.get(target_url).json()

    # Parse Data
    firstName = data["firstName"]
    lastName = data["lastName"]
    userKey = data["userKey"]
    lat = data["latitude"]
    long = data["longitude"]

    return firstName, lastName, userKey, lat, long

