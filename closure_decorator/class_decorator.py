#!/usr/bin/python

# class attribute, object attribute

def DecorateClass(cls):
    cls.added_attribute = "Decorated Attribute"
    cls.empty_list = []
    return cls

@DecorateClass
class Temp(object):
    def __init__(self):
        self.acct_no = 1
    def Display(self):
        pass

@DecorateClass
class Test(object):
    def __init__(self):
        self.id = 1
print Temp.__dict__
print Test.__dict__
t = Temp()
print t.__dict__
'''
def main():
    t = Temp()
    t1 = Temp()
    print(dir(t))
    print(id(Temp.added_attribute), id(t.added_attribute))
    t.added_attribute += " Hello"
    print(id(Temp.added_attribute), id(t.added_attribute))
    print(Temp.added_attribute, t.added_attribute)
    Temp.added_attribute += " Bye"
    print(id(Temp.added_attribute), id(t.added_attribute))
    print(Temp.added_attribute, t.added_attribute, t1.added_attribute)

    print(Temp.empty_list, t.empty_list, t1.empty_list)
    t.empty_list.append([1,2,3])
    print(Temp.empty_list, t.empty_list, t1.empty_list)
    print(id(Temp.empty_list), id(t.empty_list), id(t1.empty_list))
'''
'''
def main():
    print (id(Test.added_attribute), id(Test.empty_list))
    print(dir(Test))

    obj = Test()
    print(id(obj.added_attribute), id(obj.empty_list), id(obj.id))
    obj.added_attribute += " Hello"
    
    print(id(Test.added_attribute), id(obj.added_attribute))
    obj.empty_list.append([1,2,3])
    print(id(Test.empty_list), id(obj.empty_list))
'''
'''
@DecorateClass
class Test(object):
    pass

@Test
class MyTest:
    pass
def main():
    print (Test.added_attribute)    
    print (id(Test.added_attribute))
    print (dir(Test))
    obj = Test()
    print (id(obj.added_attribute))
    obj.added_attribute = "Changed."
    print (dir(obj))
    print(obj.added_attribute)
    print (Test.added_attribute)    
    print (id(obj.added_attribute))
    obj1 = Test()
    print (id(obj1.added_attribute))
''' 
'''
if __name__ == "__main__":
    main()
'''
