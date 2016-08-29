class Test:
	def accessible(self):
		print 'This is accessible'
	def __notaccessible(self):
		print 'This is not accessible'

Test().accessible()
Test()._Test__notaccessible()
Test().__notaccessible()
