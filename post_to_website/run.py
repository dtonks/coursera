# script allows you to turn a text file into a dictionary and post to a website using json

#!/usr/bin/env python3

import os
import requests

url = pass # enter the website you want to post to
file_location = "./txt_files/" # location of files

for file in os.listdir(file_location):
  data = {}
  keys = ["title", "name", "date", "feedback"]
  with open(file_location + file) as t:
    i = 0
    for line in t:
       data[keys[i]] = line.strip()
       i += 1
    upload = request.post(url, json=data)
