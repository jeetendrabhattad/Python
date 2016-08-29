#!/usr/bin/python

def Hello():
    print("Hello Done with Program !!!")
if __name__ == "__main__":
    number = 0
    while number != 100:
        number = int(input("Enter number (to stop enter 100):"))
        if number%5 == 0:
            print("Entered number {} is multiple of 5".format(number))
        else:
            print("Entered number {} is not multiple of 5".format(number))
    else:
        print("In Else of while")
