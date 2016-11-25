class Parent:
	'''Inheritance example'''
	property=10000000 # attribute of class
	def __init__(self): # Constructor
		print ("Parent Constructor")
		self.salary=0 # attribute of object
	def __del__(self): #  Destructor
		print ("Destroying Parent")
	def Display(self):
		print (self.property)
	def Earn(self):
		self.salary =20000
		print ("total Accomodate Salary=%d"%self.salary)
	def Savings(self):
		print ("How much Saved:%d"%self.salary)
	def TotalExpense(self,exp):
		print ("Total Expense of Parent")
		self.salary -=exp	
class Child(Parent):
	def __init__(self):
		print ("Child Constructor")
		self.standard=0
		self.consume=40000
	def __del__(self):
		print ("Destroying Child")
	def Expense(self,exp):
		super(self, Child).TotalExpense(exp)
		self.consume =exp
		self.salary -= exp
		 
obj=Child()
obj.Display()
obj.Earn()
obj.Expense(10000)
obj.Savings()
print (obj.__dict__)
	
