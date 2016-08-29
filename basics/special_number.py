#!/usr/bin/python

def Factorial(number):
    fact = 1
    for i in range(2, number+1):
        fact = fact*i
    return fact

def IsSpecial(number):
    sum_of_fact = 0
    original_number = number
    while number != 0:
        digit = number % 10
        sum_of_fact += Factorial(digit)
        number = number / 10

    return original_number == sum_of_fact

if __name__ == "__main__":
    number = input("Enter number to be checked whether special or not ?:-")
    if IsSpecial(number):
        print("Entered number {} is a special number.".format(number))
    else:
        print("Entered number {} is not a special number.".format(number))
    print("Done") 
