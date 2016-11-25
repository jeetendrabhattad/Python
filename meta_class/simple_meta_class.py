#!/usr/bin/python

'''
    Enforcing Every Class to __init__ and __del__ methods
'''

class ManagerMeta(type):
    def __init__(self, name, bases, member_dict):
        manager_init_method = False
        manager_del_method = False
        for key, value in member_dict.items():
            print(key)
            if key == "__init__":
                manager_init_method = True
            elif key == "__del__":
                manager_del_method = True
        if not manager_init_method or not manager_del_method:
            raise NameError("constructor & destructor not found")
        return type.__init__(self, name, bases, member_dict)

class Test(metaclass = ManagerMeta):
    def __init__(self):
        pass
    def __del__(self):
        pass

class Test2(metaclass = ManagerMeta):
    pass
'''
#Test = ManagerMeta('Test', (,), {'a':10, '__init__':__init__, '__del__':__del__})

class Test:
    __metaclass__ = ManagerMeta
    a = 10
    def __init__(self):
        self.b = 20
    def __del__(self):
        pass
#t = Test()
#print (t.__dict__)
#print (Test.__dict__)

#class Test3(Test):
#    pass
class Test2:
    __metaclass__ = ManagerMeta
'''
