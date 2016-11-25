class MyException(Exception):
	''' user defined exception'''
	def __init__(self, x):
		self.x = x
	def __str__(self):
		return "MyException:"+str(self.x)
		
try:
	raise MyException(10) # to throw an exception use raise
	fd = open("c.txt","r")
	try:
		fd.write("Hello")
	except Exception as e:
		print "Nested Exception :", e
	finally:
		print "Finally Invoked, Performing Cleanup"
		fd.close()
except MyException as e:
	print ("MyException Invoked")
	print e
except Exception as e:
	print ("exception block",e)	
except IOError as e:
	print (e)
	fd.close()	
except NameError as e:
	print ("Name Error", e)
'''
fd = open("a.txt","r")
fd.write("Hello")
fd.close()
'''
print("Done...")
