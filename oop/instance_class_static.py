#!/usr/bin/python

class Test(object):

    class_attribute = "hello"
    def __init__(self):
        self.object_attribute = "Happy Diwali"
    # instance methode : invoked by object 
    def Display(self):
        '''
            Display is an instance method.
            How to Invoke :
            obj = Test()
            obj.Display() or Test.Display(obj)
        '''
        print(type(self))
        print(self.object_attribute)

    @classmethod
    def DisplayCM(cls):
        '''
            DisplayCM is a class method.
            How to Invoke :
            Test.Display()
            cls is an object of type Test i.e basically it is reference to class
        '''
        print(type(cls), id(cls))
        print(cls.class_attribute)
        #Test.class_attribute
        #print(cls.object_attribute) # error as object_attribute is not of Class but of Object
    
    @staticmethod # method which is invoked without object
    def DisplayStatic():
        '''
            DisplayStatic is a static method
            How to Invoke :
            Test.DisplayStatic() or obj.DisplayStatic()
            It takes no argument as self i.e object, other arguments can be passed. Class attributes can be accessed through <class-name>.<attribute_name>
        '''
        print("Invoked Static Method, cannot access object attributes without object")

    @staticmethod
    def StaticTest(args):
        print(type(args))

def main():
    
    #Invoking Instance Method 
    print(id(Test))
    t = Test()
    t.Display()
    #Invoking Class Method
    Test.DisplayCM()
    # Ideally class methods should not be invoked using object
    t.DisplayCM() # though called using t still Test is passed as an argument to class method.
    #Invoking Static Method
    # static methods should not be invoked using object
    t.DisplayStatic()
    Test.DisplayStatic()

    Test.StaticTest([1,2,3])
    Test.StaticTest(t) # Bad practice, if a method needs object as an argument make it instance method

if __name__ == "__main__":
    main()
    print dir()
