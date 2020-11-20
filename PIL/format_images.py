#!/usr/bin/python3

'''
What do I want to do?
1. Direct to the images location - done
2. Iterate through the files - done
3. Rotate the image
4. resize the image
5. Convert image to jpeg
6. save image to ~/opt/icons
'''

from PIL import Image
import os, sys

## Allows you to run script on any folder
# for folder in sys.argv[1:]:
save_to = "./formatted"
folder = "./images"

for image in os.listdir(folder):
  rgb_img = Image.open(f"./images/{image}")
  img = rgb_img.convert("RGB")
  img.resize((128,128)).rotate(270).save(f"./formatted/{image}.jpeg")

  # rgb_img = img.convert('RGB')
  # img.convert("RGB").show()
  # print(img.mode)
  # rgb_img.save(f"./formatted/{image}.jpeg")

  # print(img.format)
  # img.resize((128,128)).rotate(270).show()
  # img.rotate(270).show()
  break
