#!/usr/bin/python

def ReferenceModel(number):
    print("ID inside function = {}, value = {}".format(id(number), number))
    number = 100
    print("After modification ID inside function = {}, value = {}".format(id(number), number))

def MultipleReturns():
    return 1,2,None

if __name__ == "__main__":
    no = int(input("Enter a number:"))
    print("You entered number %d "%(no))
    print("id = {}".format(id(no)))
    ReferenceModel(no)
    #print("You entered number %d "%(no))
    print("id = {}".format(id(no)))

    #multiple returns
    a,b,c = MultipleReturns()
    print ("return value {} {} {}".format(a,b,c))
    #anonymous variable
    _,_,c = MultipleReturns()
    print(c)
    #converting multiple returns to list
    c = list(MultipleReturns())
    print(c)
