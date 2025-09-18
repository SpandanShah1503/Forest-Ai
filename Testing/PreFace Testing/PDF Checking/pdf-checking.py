import cv2
import pytesseract
from pdf2image import convert_from_path
import json
import re
import numpy as np
import os 

#Input as sample.pdf
pdf_path = "sample.pdf"

#Folder where our output will be 
output_path = "Testing/PreFace Testing/PDF Checking/ PDF Checking - OutputData"

#Combines folder path + file name = full path 
output_json_path = os.path.join(output_path, "sample.json")


# Create processed folder if it doesn't exist
os.makedirs(output_path, exist_ok = True) 


#convert_from_path is a function from the pdf2image library
#Converts each page into an image.
pages = convert_from_path(pdf_path)

#creates a list (array) of images
images = [np.array(page) 
          for page in pages]

