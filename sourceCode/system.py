# system.py
# VALET's Raspberry Pi System, with Functions Imported
# Combines functions of:
    # Fetching JSON from URL
    # Reading Data from PiCamera for QR Code
    # Obstruction Detection
    # Accessing Lidar
    # Putting Data over SPI
# Future Improvements, as of 03/05/2020 at 2:26 AM
    # Tune up LiDAR for More Consistent Functionality
    # Putting Data over SPI
    # More advanced camera functions
    # User matching functions
    # Moving average for LiDAR
    # Timeout functions!!!
# Author: Alden Kane

#########################################
# Section 1: Import Libraries and Functions
#########################################

from get_User_Info import get_User_Info
from get_Camera import get_Camera_Headless
from get_LiDAR import get_LiDAR

#########################################
# Section 2: Declare Function Inputs
#########################################

target_URL = 'http://seniordesign.ee.nd.edu/2020/Design%20Teams/valet/users.json'

#########################################
# Section 3: Call Functions
#########################################

firstName, lastName, userKey, lat, long = get_User_Info(target_URL)
obstruction, barcodeData = get_Camera_Headless()
distance = get_LiDAR()

#########################################
# Section 4: Print for Debug
#########################################
# Print for Debug
print("system.py Block")
print("-------------------")
print("Web Fetched User Key: " + str(userKey))
print("Target Delivery Latitude: " + lat)
print("Target Delivery Longitude: " + long)
print("QR Encoded userKey: " + barcodeData)
print("Vision Based Obstruction Found: " + str(obstruction))
print("LiDAR Detection Distance: " + str(distance) + " cm")
print("")