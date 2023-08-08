
# This is a sample program for OCR using Paddle OCR lib, reading text in images.
# This program uses Paddle OCR library to perform OCR functions, we use the models to extract text from images passed.
from paddleocr import PaddleOCR, draw_ocr   # OCR library dependencies
from matplotlib import pyplot as plt  # for plotting images
import cv2  # open cv
import os  # for opening directories

ocr_model = PaddleOCR(use_angle_cls=True, lang='en')  # instantiate the model
img_path = os.path.join('.', 'SampleImage.jpeg')
print(img_path)
result = ocr_model.ocr(img_path, cls=True)
print('-------')
print(result)


