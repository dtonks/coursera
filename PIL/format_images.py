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

# ./format_images.py images

from PIL import Image
import os, sys

for file in glob.glob("ic_*"):
  rgb_img = Image.open(file)
  img = rgb_img.convert("RGB")
  img.resize((128,128)).rotate(270).save("/opt/icons/" + file, "JPEG")
