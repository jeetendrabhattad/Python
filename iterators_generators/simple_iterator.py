#!/usr/bin/python

def main(x):
    i = iter(range(x))
    print (next(i))
    print (next(i))
    print (next(i))
    print (next(i))

#boiler-plate
if __name__ == "__main__":
    main(5) 
