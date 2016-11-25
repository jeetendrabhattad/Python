#!/usr/bin/python

#decorators do not get applied in inheritance heierarchy, metaclasses get
def debugmethod(cls):
    print("debug method invoked")
    return cls

@debugmethod
class Base(object):
    pass

class Derived(Base):
    pass

#b = Base()
#d = Derived()
class DebugMethodMeta(type):
    def __init__(self, names, bases, member_dict):
        print("Debug Method Meta Invoked")
        return type.__init__(self, names, bases, member_dict)
#2.7
class BaseMeta:
    __metaclass__ = DebugMethodMeta

class DerivedMeta(BaseMeta):
    pass        
'''
class BaseMeta(metaclass = DebugMethodMeta):
    pass
class DerivedMeta(BaseMeta):
    pass        
'''
