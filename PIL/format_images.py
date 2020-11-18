#!/usr/local/bin/python3

'''
What do I want to do?
1. Direct to the images location
2. Iterate through the files
3. Rotate the image
4. resize the image
5. save image to ~/opt/icons
'''

from PIL import Image
import os, sys


for file in sys.argv[1:]:
  print(file)

