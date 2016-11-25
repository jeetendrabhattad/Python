#!/usr/bin/python

'''
    Python provides you to call any object as long as it provides the __call__() method.
    So to write a class based decorator you just need to create an object that defines such a method.
    When used as decorator a class is instantiated at decoration time i.e when the function is defined & it results into invokaction of __call__ method. 
'''
class Person(object):
    def __init__(self, name):
        '''
            Init is invoked at decoration time
        '''
        self.name = name
        print(name)
    def __call__(self, obj):
        '''
            __call__() method of the decorator is called 
        '''
        #print(obj)
        def wrap(*args):
            print(args)
            #print(type(obj))
            print ("Sample Decorator...")
            #return obj(args) # return Test(args)
            return obj(args) # return Test(args)
        return wrap

#t = Person("Jeetendra")
#t1 = t(Test)
#t2 = t1([1,2,3])

@Person("jeetendra")
class Test(object):
    def __init__(self, *args):
        print("Test Created")
        print(args)
    def Display(self):
        print("Display of Test Invoked")

if __name__ == "__main__":
    t = Test("hello", "Bye") # wrap("hello", "bye")
    t.Display()
    #print(type(t))
    #print(dir(t))
