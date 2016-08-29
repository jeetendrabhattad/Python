#!/usr/bin/python

def UniqueElementsList(l1 = []):
    l2 = []
    for x in l1:
        if x not in l2:
            l2.append(x)
    return l2

if __name__ == "__main__":
    l1 = input("Enter list of duplicate elements:")
    print("Set of input list is {}".format(set(l1)))
    l2 = UniqueElementsList(l1)
    print("Unique elements list of input list {} is \n {}".format(l1, l2))
