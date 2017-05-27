#!/usr/bin/python
'''
def Multiply(x,y):
#    print x,y
    return x*y

print reduce(Multiply, range(1,10))
'''
print reduce(lambda x,y:x*y, range(1,10))

mul = lambda x,y:x*y
print(mul(10, 20))
