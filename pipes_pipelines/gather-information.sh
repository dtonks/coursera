#!/bin/bash

'''
echo "Starting at: $(date)"

one way to do it, but using ; is cleaner
echo "UPTIME"
uptime
echo

echo "FREE"
FREE
echo

echo "WHO"
who
echo

echo "Finishing at: $(date)"

'''
# defining variable line to come after we run each line of code
line="------------------------------------------"

echo "Starting at: $(date)"

echo "UPTIME"; uptime; echo $line

echo "FREE"; FREE; echo $line

echo "WHO"; who; echo $line

echo "Finishing at: $(date)"
