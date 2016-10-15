import inspect

#class Base():
class Base(object):
    def Print(self):
        print("Print of Base")

class A(Base):
    def Display(self):
        print("Display of A")

    def Foo(self):
        print("In Foo")

class B(Base):
    def Print(self):
        print("Print of B")
    
    def Display(self):
        print("Display of B")

class C(A, B):
    pass
    #def Display(self):
    #    print("Display of C")
class D(B, A):
    pass

x = C()
x.Display()
x.Print()
'''
z = D()
z.Display()
z.Print()
z.Foo()
'''
print(inspect.getmro(C))
