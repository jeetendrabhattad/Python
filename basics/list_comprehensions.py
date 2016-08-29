#print [x**2 for x in range(10)]
#print [(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y]

import math
from random import choice

def isSquare( x ):
    sqrt = int(math.sqrt(x))
    return x == sqrt*sqrt
   # sqrt = int(math.sqrt(x))
   # print sqrt, x
   # return x%sqrt == 0
    print [ x for x in range(1,101) if isSquare(x) == True]

    print [x + y for x in range(10) for y in range (x) if x-1 == y]

def Random57Divisible(n):
    return choice([x for x in range(n) if x%5 == 0 and x%7==0])

print (Random57Divisible(10000))
