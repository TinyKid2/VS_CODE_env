import easyOCR
import easyocr
import cv2
import matplotlib.pyplot as plt
reader = easyocr.Reader(['ko','en'])


impath = 'vscode/OCR.py/IMG_2384.JPG'

img = cv2.imread(impath)
result = reader.readtext(impath)

THR = 0.5
result1 = ''
for bbox, text, conf in result:
  if conf > THR:
    result1 = result1 + text

result = result1.split(' ')
print(result)
