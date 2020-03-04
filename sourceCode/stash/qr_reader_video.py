# qr_reader_video.py
# A script to read QR codes from Webcam. Will be made into function
# EE Senior Design: Team Valet
# Referenced Adrian Rosebrock's "An OpenCV barcode and QR code scanner with ZBar" at https://www.pyimagesearch.com/2018/05/21/an-opencv-barcode-and-qr-code-scanner-with-zbar/
#   Author: Alden Kane

from pyzbar import pyzbar
import cv2

######################################
# Section 1: Preprocessing
######################################
# Get video stream from Webcam
cam = cv2.VideoCapture(0)

######################################
# Section 2: QR Code Reading, turn into function
######################################

# While loop to detect and iterate through barcodes
while(True):
    # Read from camera
    retval, img = cam.read()

    # Rescale if too large
    res_scale = 0.5
    img = cv2.resize(img, (0, 0), fx=res_scale, fy=res_scale)

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

    # Show
    cv2.imshow("QR Code Detection", img)
    key = cv2.waitKey(1) & 0xFF

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break

cv2.destroyAllWindows()