class __Private:
    def __init__(self):
        self.a = 10
    def Display(self):
        print self.a
class Test(__Private):
    def __init__(self):
        #__Private.__init__(self)
        #super(__Private, self).__init__()
        self.b = 20

b = __Private()
b.Display()
print b.__dict__
c = Test()
print Test.__dict__
print c.__dict__

