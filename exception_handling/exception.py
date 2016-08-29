#!/usr/bin/python

def DemoException():
	try:
		w = open('b.txt', 'r')
		try:
			w.write("Jay Shri Ram")
		finally:
			print"Closing The File\n"
			w.close()
	except list((IOError, NameError, TypeError)):
		print 'Error'
	except IOError, argument:
		print "IOError ", argument

def RaiseExceptionDemo(level):
	if level < 1:
		raise Exception('InvalidLevel', level)

def TestRaise():
	try:
		level = input("Enter Level")
		RaiseExceptionDemo(level)
	except Exception as inst:
		print 'Exception Recvd ', inst.args

DemoException()
TestRaise()
