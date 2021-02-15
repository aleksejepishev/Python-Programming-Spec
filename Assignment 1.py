#!/usr/bin/env python
# coding: utf-8

# In[75]:


from PIL import Image
from PIL import ImageEnhance
from PIL import ImageDraw
from PIL import ImageFont

image = Image.open('cat.jpg')
image = image.convert('RGB')
font = ImageFont.truetype('fanwood-webfont.ttf', 50)
chanels = [0, 1, 2]
inten = [0.1, 0.5, 0.9]

def changeimage(c, i):
    words_area = Image.new('RGB', (image.width, 50))
    words = ImageDraw.Draw(words_area)
    words.text((0,0), f'chanel{chanels[c]} intensity {inten[i]}', font = font)
    
    background = Image.new('RGB', (image.width, image.height + 50))
    background.paste(image, (0,0))
    background.paste(words_area, (0, image.height + 3))
    
    splitted = list(background.split())
    splitted[chanels[c]] = splitted[chanels[c]].point(lambda x: x * inten[i])
    new_image = Image.merge('RGB', splitted)
    return new_image

images = [changeimage(c, i) for c in range(3) for i in range(3)]
first_image=images[0]
contact_sheet=PIL.Image.new(first_image.mode, (first_image.width*3,first_image.height*3))
x = 0
y = 0

for img in images:
    sheet.paste(img, (x, y))
    if x+first_image.width == sheet.width:
        x = 0
        y = y + first_image.height
    else:
        x = x + first_image.width

contact_sheet = sheet.resize((int(sheet.width/2),int(sheet.height/2) ))
contact_sheet


# In[ ]:




