#!/usr/bin/python

def MixUp(a, b):
	return b[:2]+a[2:]+" "+a[:2]+b[2:]

print( MixUp("mid", "pox"))
