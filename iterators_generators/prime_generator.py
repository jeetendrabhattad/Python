#!/usr/bin/python
import math

def IsPrime(number):
    retVal = False
    if number > 1:
        if number == 2:
            retVal = True
        if not number & 1:
            retVal = False
        else:
            for divisor in range(3, int(math.sqrt(number)+1), 2):
                if number % divisor == 0:
                    retVal = False
                    break
            else:
                retVal = True
    return retVal 

def GetPrimes(inputList):
    for number in inputList:
        if IsPrime(number):
            yield number

def main():
    x = GetPrimes(range(1, 100))
    print (type(x))
    print (next(x))
    print (next(x))
    #for y in x:
    #    print (y)

if __name__ == "__main__":
    main()  
