#!/usr/bin/python
from foo import foo
a = 100
def test():
    print("test of bar")

def bar():
    global a
    print(a)
    foo()
    print(a)
    test()

if __name__ == "__main__":
    bar()
    
