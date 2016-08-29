#!/usr/bin/python
def IsAllDigitsEven(number):
    while number:
        digit = number % 10
        if digit & 1:
            return False
        number = number // 10
    return True

def EvenDigitsNumberInRange(lb, ub):
    result = []
    for number in range(lb, ub+1):
        if IsAllDigitsEven(number):
            result.append(number)
    return result

if __name__ == "__main__":
    print("Program to print list of even digits numbers in the given range....")
    lb = input("Enter lower bound of the range:")
    ub = input("Enter upper boung of the range:")
    print(EvenDigitsNumberInRange(lb, ub))
