def Factorial(number):
    if number < 0:
        return "Cannot Find Factrial of Negative Number"
    if number == 0 or number == 1:
        return 1
    return number*Factorial(number - 1)

if __name__ == '__main__':
    number = input("Enter Number to find factorial:")
    print(Factorial(number))

