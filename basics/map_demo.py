#!/usr/bin/python

def Square(x):
    return x*x

#x = map(Square, range(1, 30, 2))
x = map(lambda x:x*x, range(1, 30, 2))
print (x)
#help(x)
'''
l1 = []
for x in range(1,30,2):
    l1.append(Square(x)
return l1
'''
