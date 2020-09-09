# Getting environment variable from your python scripts

#! /usr/bin/env python3

import os

print("HOME: " + os.environ.get("HOME", ""))
print("SHELL: " + os.environ.get("SHELL", ""))

# define the variable
# in termial:
# export FRUIT=Pineapple
print("FRUIT: " + os.environ.get("FRUIT", ""))
