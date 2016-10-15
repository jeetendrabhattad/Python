#!/usr/bin/python
print("If Else Demo Module ", __name__)

def Hello():
    print("Hello Done with Program !!!")

def Add(a, b):
    return a + b

def Sub(a, b):
    return a - b

def main():
    number = 0
    while number != 100:
        number = int(input("Enter number (to stop enter 100):"))
        if number%5 == 0:
            print("Entered number {} is multiple of 5".format(number))
        else:
            print("Entered number {} is not multiple of 5".format(number))
    else:
        print("In Else of while")
    print(Add(10, 20))
    print(Sub(20, 10))

if __name__ == "__main__":
    main()
