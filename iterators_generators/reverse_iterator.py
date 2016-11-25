#!/usr/bin/python

class ReferenceCount:
    def __init__(self, start):
        self.start = start
    
    #Forward Iterator
    def __iter__(self):
        start = self.start
        while start > 0:
            yield start
            start -= 1
    
    def __reversed__(self):
        start = 1
        while start <= self.start:
            yield start
            start += 1

def main():
    x = ReferenceCount(10)
    print("Display from 10---1")
    for y in x:
        print (y)
    
    print("Display from 1---10")
    for w in reversed(x):
        print(w)

if __name__ == "__main__":
    main()
