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
	def ValidatePassword(self, password):
		for p in password:
			if re.search("[a-z]", p) :
				print("Password Contains Small Case Characters")
			elif re.search("[A-Z]", p):
				print("Password Contains Capital Case Characters")
			elif re.search("[@#$]", p):
				print("Password Contains Special Characters")
			elif re.search("[0-9]", p):
				print("Password Contains Integers")
		return password
	def SetPassword(self, password):
		if self.ValidatePassword(password):
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
