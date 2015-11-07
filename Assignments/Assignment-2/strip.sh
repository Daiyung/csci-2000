#!/bin/bash
# Name: Dai Vincent Chan
# Student ID: 100 554 446

#removes leading 'k' number of lines and trailing 'm' lines
#from a text file, prints result to screen

 head -n-$2 $3 | tail -n +$1
