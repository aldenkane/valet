### subsystem_PiCam.py
### VALET's subsystem demo for the end of Semester 1 in University of Notre Dame's EE 41430: Senior Design Class
### Code designed to detect QR Code for final handoff of VALET delivery between robot and customer, as well as detection major obstructions
### Major obstruction detection used as a redundant sensor for our distance sensor. Operates by taking the standard deviation of all pixel values on screen
###     Author: Alden Kane

import cv2 as cv2
from pyzbar import pyzbar


######################################
### Section 1: Preprocessing
######################################
# Get video stream from Webcam
cam = cv2.VideoCapture(0)

# While loop to detect and iterate through barcodes
while(True):
    # Read from camera
    retval, img = cam.read()

    # Rescale if too large
    res_scale = 0.5
    img = cv2.resize(img, (0, 0), fx=res_scale, fy=res_scale)

    ################################################
    ### Section 2: QR Code Recognition
    ################################################
    # Find + decode barcodes
    barcodes = pyzbar.decode(img)

    # Iterate over barcodes
    for barcode in barcodes:
        # Get bounding box
        (x, y, w, h) = barcode.rect

        # Get information on barcodes
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type

        # Only interested in QRCODE recognition
        if (barcodeType == 'QRCODE'):
            # Draw bounding box, and put text next to it
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
            text = "{} ({})".format(barcodeData, barcodeType)
            cv2.putText(img, text, (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    ################################################
    ### Section 3: Objection Detection
    ################################################
    # Calculate mean and standard deviation of image
    mean, std = cv2.meanStdDev(img)

    # Obstruction Calculation
    if std[0] < 30 or std[1] < 30 or std[2] < 30:
        obstruction = 1
    else:
        obstruction = 0

    obstruction_text = "Obstruction Value ({})".format(obstruction)

    # Put text
    cv2.putText(img, str(mean), (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.putText(img, str(std), (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.putText(img, obstruction_text, (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # Show Image Feed
    cv2.imshow("Subsystem", img)
    key = cv2.waitKey(1) & 0xFF
