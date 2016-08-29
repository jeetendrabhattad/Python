#!/usr/bin/python

def Factorial(number):
    fact = 1
    for i in range(2, number+1):
        fact = fact*i
    return fact

def IsSpecial(number):
    print("Incorrect Isspecial Invoked")
    return True

if __name__ == "__main__":
    number = input("Enter number to be checked whether special or not ?:-")
    if IsSpecial(number):
        print("Entered number {} is a special number.".format(number))
    else:
        print("Entered number {} is not a special number.".format(number))
    print("Done") 
