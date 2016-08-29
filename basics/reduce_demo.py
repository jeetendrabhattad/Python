#!/usr/bin/python

def Multiply(x,y):
#    print x,y
    return x*y

print reduce(Multiply, range(1,10))
