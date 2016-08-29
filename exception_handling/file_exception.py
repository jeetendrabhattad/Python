#!/usr/bin/python

try:
    fd = open("a","r")
except Exception as e:
#    print e.__getattribute__('name')
    print( e.errno )
    print e.args
    print type(e).__name__
