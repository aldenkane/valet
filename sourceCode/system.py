# system.py
# VALET's Raspberry Pi System, with Functions Imported
# Combines functions of:
    # Fetching JSON from URL
    # Reading Data from PiCamera for QR Code
    # Obstruction Detection
    # Accessing Lidar
    # Putting Data over SPI
# Author: Alden Kane

#########################################
# Section 1: Import Libraries and Functions
#########################################

from get_User_Info import get_User_Info
from get_Camera import get_Camera
from get_LiDAR import get_LiDAR

#########################################
# Section 2: Declare Function Inputs
#########################################

target_URL = 'http://seniordesign.ee.nd.edu/2020/Design%20Teams/valet/users.json'

#########################################
# Section 3: Call Functions
#########################################

firstName, lastName, userKey, lat, long = get_User_Info(target_URL)
distance = get_LiDAR()
obstruction, barcodeData = get_Camera()


#########################################
# Section 4: Print for Debug
#########################################
# Print for Debug
print("system.py Block")
print("-------------------")
print("User Key: " + str(userKey))
print("Latitude: " + lat)
print("Longitude: " + long)
print("QR Encoded userKey " + barcodeData)
print("LiDAR Detection Distance: " + distance)
print("")