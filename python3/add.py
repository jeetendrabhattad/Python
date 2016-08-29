#!/usr/bin/python

def HelloWorld():
    print("Hello World !!!")

def Add(a=10, b=2):
    return a+b

def Multiply(a, b):
    return a*b
print "India"
if __name__=='__main__':
    HelloWorld()
    print(Add(10, 20))
    print(Add(100))
    print(Add())
    a = (input("Enter String"))
    print a, type(a)
    print(Multiply(10,2))

