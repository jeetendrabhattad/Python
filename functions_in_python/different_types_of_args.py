#!/usr/bin/python

def PositionalArgumentDemo(number1, number2):
    print(number1, number2)

PositionalArgumentDemo(10, 20)

def DefaultArgumentDemo(num1, num2, num3 = 0, num4 = 0, num5 = 0):
    print (num1+num2+num3+num4+num5)

DefaultArgumentDemo(10, 20, 30)
DefaultArgumentDemo(10, 20)

def KeywordArgumentDemo(number1, number3, number2):
    print(number1, number2)

KeywordArgumentDemo(20, number2=10, number3=20)

def VariableArgumentsDemo(a,b,*args):
    print(type(args))
    for x in args:
        print (x)

VariableArgumentsDemo(1,2)
VariableArgumentsDemo(1,3)
VariableArgumentsDemo(1,2)
VariableArgumentsDemo(1,2,3,4,5,6)

def VariableDictionaryArgumentsDemo(n1,n2,a,b,*args, **kwargs):
    for x in args:
        print(x)
    for x in kwargs:
        print(x, kwargs[x])

VariableDictionaryArgumentsDemo(1,2,20,10,1,2,3,4, name="Jeetendra", surname="Bhattad", age="29")
