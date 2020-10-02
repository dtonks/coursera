#!/usr/bin/env python3

import sys
import subprocess

with open(sys.argv[1], 'r') as f:
  for line in f.readlines():
    old = line.strip()
    new = old.replace("jane", "jdoe")
    subprocess.run(['mv',old,new])
