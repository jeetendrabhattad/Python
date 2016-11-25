#!/usr/bin/python

'''
    Python provides you to call any object as long as it provides the __call__() method.
    So to write a class based decorator you just need to create an object that defines such a method.
    When used as decorator a class is instantiated at decoration time i.e when the function is defined and
    called when the function is called
'''
class Person(object):
    def __init__(self, name):
        '''
            Init is invoked at decoration time
        '''
        self.name = name
        #self.obj = obj
    def __call__(self, obj):
        '''
            __call__() method of the decorator is called 
        '''
        print(obj)
        obj()
    def display(self):
        print ("Display Invoked")

def Print():
    print("All are in Diwali Mood")

#temp = Person("Jeetendra")
#t1 = temp(Print)
#t1()
@Person("jeetendra") 
def Display():
    print("This is that reference")
