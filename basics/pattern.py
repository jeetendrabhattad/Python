#!/usr/bin/python
def pattern1(noOfRows):
	for i in range (noOfRows):
		for j in range (i+1):
			print '*',
		print

def pattern2(noOfRows):
	for i in range (noOfRows):
		for j in range (1, i+2):
			print j,
		print

def pattern3(noOfRows):
	for i in range (noOfRows+1):
		for j in range (noOfRows - i):
			print ' ',
		for k in range (i):
			print '*',
		print

def pattern4(noOfRows):
    '''
        pattern4 is like following
               *
              ***
             *****
            *******
    '''

    for i in range (1, noOfRows+1):
		for j in range (noOfRows - i):
			print ' ',
		for k in range (i*2 - 1):
			print '*',
		print

pattern1(5)
pattern2(5)
pattern3(5)
pattern4(5)
#help(pattern4)
