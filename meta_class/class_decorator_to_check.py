#!/usr/bin/python

# Decorator functions apply only when an Object gets created as it requires an explicit calling to the wrapper function
def VerifyManagerMethods(cls):
    def wrapper():
        manager_init_method = False
        manager_del_method = False
        print (cls.__dict__)
        for key in cls.__dict__.iterkeys():
            if key == "__init__":
                manager_init_method = True
            elif key == "__del__":
                manager_del_method = True
        if not manager_init_method or not manager_del_method:
            raise NameError("constructor or destructor not found")
        else:
            print("Constructor & Destructor Found")
        return cls
    return wrapper


@VerifyManagerMethods
class Test2:
    def __init__(self):
        pass
    def __del__(self):
        pass

t2 = Test2()

@VerifyManagerMethods
class Test:
    pass

t = Test() 
