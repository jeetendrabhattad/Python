#!/usr/bin/python
def max3(x, y, z):
	if x > y and x > z:
		print '%d is greater than %d %d\n'%(x,y,z)
	elif y > z:
		print '%d is greater than %d %d\n'%(y,x,z)
	else:
		print '%d is greater than %d %d\n'%(z,x,y)
