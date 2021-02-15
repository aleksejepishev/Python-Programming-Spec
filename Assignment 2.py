#!/usr/bin/env python
# coding: utf-8

# In[1]:


#our task is to write python code which allows one to search through the images 
#looking for the occurrences of keywords and faces. 
#E.g. if you search for "pizza" it will return a contact sheet of all of the faces 
#which were located on the newspaper page which mentions "pizza".
import zipfile
import cv2 as cv
from PIL import Image
from PIL import ImageDraw
import numpy as np
import pytesseract

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# In[2]:


#text processing
def text_processing(img):
    gray = img.convert('1')
    text = pytesseract.image_to_string(gray)
    splitted = text.split('\n')
    joined = " ".join(splitted)
    return joined.strip()


# In[3]:


#image processing
def image_processing(cv_img):
    gray = cv.cvtColor(cv_img, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)
    faces = face_cascade.detectMultiScale(cv_img,1.35)
    return faces


# In[4]:


#image croping
def image_croping(img, boundaries):
    img = img.crop((boundaries[0], boundaries[1], boundaries[0] + boundaries[2], boundaries[1] + boundaries[3]))
    img = img.resize((285, 285))
    return img

#sheet doing
def contact_sheet(imgs):
    sheet = Image.new(imgs[0].mode, (imgs[0].width * (len(imgs)//2), imgs[0].height * 2))
    x = 0
    y = 0
    for img in imgs:
        sheet.paste(img, (x, y))
        if x + imgs[0].width == sheet.width:
            x = 0
            y = y + imgs[0].height
        else:
            x = x + imgs[0].width
    return sheet


# In[5]:


#user guess check

zp_files = zipfile.ZipFile('small_img.zip')
zp_files.extractall()
list_files = zp_files.namelist()

def image_reading():
    imgs = []
    user_guess = input('Enter your inquiry: ')
    for i in list_files:
        img = Image.open(i)
        cv_img = cv.imread(i)
        if user_guess in text_processing(img):
            faces = image_processing(cv_img)
            for i in range(len(faces)):
                imgs.append(image_croping(img, faces[i]))
        else:
            print('Nothing found!')
    sheet = contact_sheet(imgs)
    sheet = sheet.resize((int(sheet.width/2),int(sheet.height/2) ))
    return sheet
        
image_reading()    

