#!/usr/bin/python
""" Simple Program to Test Python is Working.
To run this program from command line:
  python hello.py
  python hello.py Jeetendra
That should print:
  Hello World or Hello Jeetendra
"""

import sys

#define main function 
def main():
	if len(sys.argv) >= 2:
		name = sys.argv[1]
	else:
		name ='World'
	print ('Hello', name)

main()
