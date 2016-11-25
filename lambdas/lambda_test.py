#!/usr/bin/python

# Lambdas are useful for creating Anonymous Functions

def Square(x):
    return x*x

x = lambda y: y*y

print(x(3))
