import cv2
import numpy as np
from pyzbar.pyzbar import decode
from PIL import Image

def barcodeDecoder(image):

    img = cv2.imread(image)             #reads the image in numpy array
    barcodes = decode(img)              #decodes barcode 
    for obj in barcodes:       

        (x, y, w, h) = obj.rect         #locating barcode in image
        #cv2.rectangle(img, (x-10, y-10), (x+(w+10), y+(h+10)), (255, 0, 0), 2)

        #if obj.data!="":
        print(obj.data)
        print(obj.type)

image = "qrcode.jpg"
barcodeDecoder(image)
#nothing
