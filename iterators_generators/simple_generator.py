#!/usr/bin/python

def SampleGenerator():
    yield 1
    yield 2
    yield 3
    yield 4

if __name__ == "__main__":
    x = SampleGenerator()
    print(next(x))
    print(next(x))
    print(next(x))
    print(next(x))
    print(next(x))
    #for x in SampleGenerator():
    #    print (x)
    #g = (x*x for x in range(1, 10))
    #print (g)
    #for x in g:
    #    print(x)
