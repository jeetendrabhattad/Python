#!/usr/bin/python
'''
def InitGenerator(func):
    def initialize():
        gen = func()
        next(gen)
        return gen
    return initialize
'''
def WrapperCoroutine(func):
    def init(*args, **kwargs):
        x = func(*args)
        next(x)
        return x
    return init

@WrapperCoroutine
def ToUpper():
    #print(args)    
    while True:
        string = yield # coroutines
        print(string.upper())
'''
z = WrapperCoroutine(ToUpper)
y = z([1,2,3])
y.send("Hello")
'''
#z = ToUpper([1,2,3])
z = ToUpper()
#next(z)
z.send("Hello")
z.send("Lloyd Electric")
print z.__name__
'''
z = ToUpper()
next(z)
z.send("Hello")
z.send("Happy Deewali")
'''

'''
@InitGenerator
def ToUpperDecorated():
    while True:
        string = yield
        print(string.upper())
'''
'''
y = InitGenerator(ToUpper)
x = y()
x.send("Hello")

x = ToUpperDecorated()
x.send("hello")
x.close()
#x.send("hello") #StopIteration
#print (x.send("hello"))
'''
