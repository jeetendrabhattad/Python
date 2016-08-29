class Person:
	x = 10
	def __init__(self):
		self.A = 'hello'
		self.__B = 'Bye'
		self.x = 200
        x = 20

    def __PrivateFoo(self):
        print("Private Foo\n")

    def PrintName(self):
		print self.A
		print self.__B
        self.__PrivateFoo()

P = Person()
print P.A
print P.PrintName()
print Person.x
print P.x
P.__PrivateFoo()
print P.__B
