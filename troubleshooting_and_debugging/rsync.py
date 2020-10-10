#!/usr/bin/env python

''' Sync or Copy data from different multimedia projects from the source
location to the destination using rsync '''

import subprocess
import os
from multiprocessing import Pool

def backup(src):
  dest = os.getcwd() + "/data/prod_backup"
  subprocess.call(['rsync', '-arq', src, dest])

if __name__ == "__main__":
  src = os.getcwd() + "/data/prod"
  files = os.listdir(src)
  all = []

  for file in files:
    path = os.path.join(src, file)
    all.append(path)

  p = Pool(len(all))
  p.map(backup, all)

