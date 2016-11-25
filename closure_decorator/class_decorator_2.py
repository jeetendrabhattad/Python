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
        def wrap():
            self.display()
            #obj()
            print ("Sample Decorator...")
        return wrap
    def display(self):
        print ("Happy Deewali")

#t = Person("Jeetendra")
#Display = t(Display)
#Display()
@Person("jeetendra")
def Display():
    print("Display Invoked")

if __name__ == "__main__":
    Display()


