#!/bin/bash

if grep "127.0.0.1" /etc/hosts; then
  echo "Everything ok"
else
  echo "ERROR! 127.0.0.1 is not in /etc/hosts"
fi


# another, seperate, example
if test -n "$PATH"; then echo "Your path is not empty"; fi
# use brackets instead of test
if [ -n "$PATH" ]; then echo "Your path is not empty"; fi
