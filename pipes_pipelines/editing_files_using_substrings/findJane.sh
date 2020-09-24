#!/bin/bash

files="$(grep ' jane ' ~/data/list.txt | cut -d '/' -f 3)"
echo $files

for file in $files; do
  if test -e ~/data/$file; then echo ~/data/$file > oldFiles.txt;
  else echo "File doesn't exist"; fi
done
