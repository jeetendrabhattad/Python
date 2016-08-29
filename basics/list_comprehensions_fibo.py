#!/usr/bin/python

def Fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return Fibo(n-1)+Fibo(n-2)

print(Fibo(7))
'''
l1 = []
for i in range(11):
    x = Fibo(i)
    l1.append(x)
print l1
'''
print( [Fibo(x) for x in range(11)])
