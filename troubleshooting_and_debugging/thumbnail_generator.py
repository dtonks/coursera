#!/usr/bin/env python3

from concurrent import futures
import argparse
import logging
import os
import sys

import PIL
import PIL.Image

from tqdm import tqdm

def process_options():

  kwargs = {
      'format': '[%(levelname)s] %(message)s'
  }

  parser = argparse.ArgumentParser(
      description='Thumbnail_generator',
      fromfile_prefix_chars='@'
  )
  parser.add_argument('--debug', action='store_true')
  parser.add_argument('-v', '--verbose', action='store_true')


def progess_bar(files):
  return tqdm(files, desc='Processing', total=len(files), dynamic_ncols=True)

def main():

  process_options()

  # Create the thumbnails directory
  if not os.path.exists('thumbnails'):
    os.mkdir('thumbnails')

  # Using executor to run things in parallel
  # ThreadPoolExecutor are slightly slower because they use saftey features to avoid having two threads try to write to the same variable
  # Proccess are faster because it uses more cpu and do not have the safety features

  # executor = futures.ThreadPoolExecutor()
  executor = futures.ProcessPoolExecutor()
  for root, _, files in os.walk('images'):
    for basename in progress_bar(files):
      if not basename.endswith('.jpg'):
        continue
      executor.submit(process_file, root, basename)
  print('Waiting for all threads to finish.')
  executor.shutdown()
  return 0


if __name__ == "__main__":
  sys.exit(main())
