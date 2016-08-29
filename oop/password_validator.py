#!/usr/bin/python
import re
class LoginDetails:
	def __init__(self):
		self.username = ""
		self.password = ""
	def __del__(self):
		print("In Destructor")
	def GetUserName(self):
		return self.username
	def GetPassword(self):
		return self.password
	def __str__(self):
		return "Username:-"+self.username+" Password:-"+self.password
	def SetUserName(self, username):
		self.username = username
	def __ValidatePassword(self, password):
		if re.search("[a-z]", password) :
			print("Password Contains Small Case Characters")
			if re.search("[A-Z]", password):
				print("Password Contains Capital Case Characters")
				if re.search("[@#$]", password):
					print("Password Contains Special Characters")
					if re.search("[0-9]", password):
						print("Password Contains Integers")
					else:
						return False
				else:
					return False
			else:
				return False
		else:
			return False
		return password
	def SetPassword(self, password):
		if self.__ValidatePassword(password):
			self.password = password
			return True
		else:
			return False

if __name__ == '__main__':
	ld = LoginDetails()
	username = raw_input("Enter username:-")
	password = raw_input("Enter password:-")
	ld.SetUserName(username)
	if ld.SetPassword(password):
		print("You have entered valid password")
	else:
		print("Invalid password, please try again")
