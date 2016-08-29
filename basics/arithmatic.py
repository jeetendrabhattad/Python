#!/usr/bin/python
def Add(a,b):
	return a+b
def Sub(a,b):
	return a-b

if __name__=="__main__":
	print("Result of addition %d"%Add(10, 20))
	print("Result of subtraction %d"%Sub(30, 20))
else:
	print("Loaded as a module")
