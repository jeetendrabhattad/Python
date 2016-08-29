def MyLength(string):
	count = 0
	for _ in string:
		count += 1
	return count

if __name__=="__main__":
	print(MyLength("Jeetendra"))
