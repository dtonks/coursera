#!/usr/bin/env python3

import sys

for line in sys.stdin:
  print(line.strip().capitalize())


# using the below command in the termianl you run the above script on the file haiku.txt:
#   cat haiku.txt | python3 capitalize.py

# can also use
#   python3 capitalize.py < haiku.txt
