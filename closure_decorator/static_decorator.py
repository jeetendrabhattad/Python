#!/usr/bin/python

class Test(object):

    @classmethod #c.Display()
    def Display(self):
        print(id(self))
        print("Display")

    @staticmethod    
    def Foo():
        print("Static Method")

    def InstanceDisplay(self):
        print("Instance Display")
#c = Test()
#c.InstanceDisplay()
#Test.InstanceDisplay(c)
#c.f()
#Test.f()
#c.Foo()
#Test.Foo()
#c.Display()
#c = Test()
#c.Display()
#Test.Display(c)
Test.Display() # t = Test() t.Display() del t
#c.f()
'''
class TestStaticDecorator(object):
    @staticmethod
    def Foo():
        print("Static Method")

c = TestStaticDecorator()
c.Foo()

class TestStatic():
    def Foo():
        print("Static Method")
    f = staticmethod(Foo)
c = TestStatic()
#TestStatic.Foo()
#c.Foo()
c.f()
'''
