#!/usr/bin/python

def Add(no1, no2):
    return no1+no2

def Sub(no1, no2):
    return no1-no2

def Mul(no1, no2):
    return no1*no2

def Div(no1, no2):
    return no1/no2

if __name__ == '__main__':
    print("Result of addition is %d"%Add(10, 20))
    print("Result of div is {}".format(Div(200, 5)))
