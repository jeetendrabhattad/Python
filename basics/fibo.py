#!/usr/bin/python
def fibonacci( n ):
    '''
        0,1,1,2,3,5,8,13,21,34....
        enter value of n >= 2
    '''
    a,b = 0,1 # multiway assignment
    print 0
    print 1
    n = n - 2
    while n:
        c = a+b
        print c
        a = b
        b = c
        n -= 1

fibonacci(15)
