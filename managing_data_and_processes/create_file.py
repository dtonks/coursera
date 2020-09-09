'''
This script receives a file name as a command line argument.
It first checks whether the file name exist or not.
When the file doesn't exist, it creates it by writing a line to it.
When the file exist, our script prints an error message and exits with an exit value of one '''


#!/usr/bin/env python3

import os
import sys

filename = sys.argv[1]

if not os.path.exists(filename):
  with open(filename, 'w') as f:
    f.write('New file created\n')
else:
  print(f'Error, the file {filename} already exists!')
  sys.exit(1)


'''
In terminal:

python3 create_file.py example (run the script, looking for file 'example')
- returns nothing

echo $?
- 0

cat example (make file 'example')

python3 create_file.py example (once again search for 'example')
- returns what our script says: 'Error, the file example already exists'

echo $?
- 1 (what our script says to output)
'''
