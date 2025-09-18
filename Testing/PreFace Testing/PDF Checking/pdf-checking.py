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



#####################################

def preprocess_and_ocr(img):
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Denoise
    gray = cv2.medianBlur(gray, 3)
    # Adaptive threshold
    gray = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                 cv2.THRESH_BINARY, 11, 2)
    # OCR
    text = pytesseract.image_to_string(gray, lang="eng")  # Change lang="hin" for Hindi
    return text

ocr_text = ""
for img in images:
    ocr_text += preprocess_and_ocr(img) + "\n"

print("----- OCR Output -----")
print(ocr_text)

# ---------- Step 3: Extract Fields with Regex ----------
data = {
    "patta_id": re.search(r"Patta ID[:\s]+(\w+)", ocr_text, re.IGNORECASE).group(1)
                if re.search(r"Patta ID[:\s]+(\w+)", ocr_text, re.IGNORECASE) else "",
    "holder_name": re.search(r"Name[:\s]+(.+)", ocr_text, re.IGNORECASE).group(1).strip()
                   if re.search(r"Name[:\s]+(.+)", ocr_text, re.IGNORECASE) else "",
    "village": re.search(r"Village[:\s]+(.+)", ocr_text, re.IGNORECASE).group(1).strip()
               if re.search(r"Village[:\s]+(.+)", ocr_text, re.IGNORECASE) else "",
    "area": re.search(r"Area[:\s]+([\d.]+)", ocr_text, re.IGNORECASE).group(1)
            if re.search(r"Area[:\s]+([\d.]+)", ocr_text, re.IGNORECASE) else ""
}

# ---------- Step 4: Save JSON ----------
with open(output_json_path, "w") as f:
    json.dump(data, f, indent=2)

print(f"✅ JSON saved at {output_json_path}")

