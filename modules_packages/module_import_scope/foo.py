#!/usr/bin/python

a = 10
def test():
    print("test of foo")
def foo():
    global a
    print(a)
    a = 20
    print(a)
    test()

if __name__ == "__main__":
    foo()
