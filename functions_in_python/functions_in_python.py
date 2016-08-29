def DefaultArgumentDemo(a, b=10):
	''' Default Argument Function Demo 
		e.g DefaultArgumentDemo(10) with 1 parameter
		or DefaultArgumentDemo(10, 20) with 2 parameters
	'''
	if b != 10:
		print 'Value of b passed %d'%b
	else:
		print 'Default Value of b is %d'%b
	print 'Value of a passed %d'%a
'''
DefaultArgumentDemo(10,20)
DefaultArgumentDemo(10)
# key value pairwise variable assignment
DefaultArgumentDemo(b=100,a=10)
#help(DefaultArgumentDemo)
'''

def VariableArgumentDemo(*args):
	''' Variable Number of Arguments of Demo '''
	for x in args:
		print x
	else:
		print 'Executing else'
'''
VariableArgumentDemo(1,2,3,4)
VariableArgumentDemo(1,2,3,4,5,6,7,8)
'''
def VariableArgumentDictionaryDemo(a,b,*args,**xargs):
	''' Variable number of arguments & dictionary '''
	print 'Value of a is %d'%a
	print 'Value of b is %d'%b
	
	for x in args:
		print x

	for x in xargs:
		print x, xargs[x]

VariableArgumentDictionaryDemo(1,2,1,2,3,name="Jeetendra", Surname="Bhattad")
#VariableArgumentDictionaryDemo(1,2,name="Jeetendra", Surname="Bhattad")
