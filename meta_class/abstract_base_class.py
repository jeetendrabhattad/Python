#!/usr/bin/python

from abc import ABCMeta, abstractmethod, abstractproperty

#class Test():
class Test(metaclass=ABCMeta):
#class Test:
#    i__metaclass__ = ABCMeta
    @abstractmethod
    def Bar(self):
        pass
    @abstractproperty
    def Foo(self, a, b):
        pass

    def Display(self):
        pass
#x = Test()
class Derived(Test):
    pass

class Derived1(Test):
    def Bar(self, ab):
        pass
    def Foo(self):
        pass

t1 = Derived1()
t = Derived()
