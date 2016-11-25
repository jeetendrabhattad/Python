#!/usr/bin/python
import pdb
import traceback

def Factorial(n):
    if n == 0 or n == 1:
        return 1
    if n == 2:
        #pdb.set_trace()
        return 2
    traceback.print_stack()
    return n*Factorial(n-1)

def main():
    number = input("Enter Number:")
    print(Factorial(number))

if __name__ == "__main__":
    main()
