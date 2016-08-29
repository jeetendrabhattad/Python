#!/usr/bin/python

def	CheckAndReturnListOfDivisibleBy(divisible, input_data):
	items = input_data.split(',')
	result = []
	for i in items:
		x = int(i, 2)
		if x%divisible == 0:
			result.append(i)
	return ",".join(result)	

if __name__ == '__main__':
	divisible = input("Enter number of whose divisibility is to be checked:")
	input_data = raw_input("Enter , separated 4 digit binary numbers to check if divisible by {} :".format(divisible))
	print("Binary numbers which are divisible by {} are {}".format(divisible,CheckAndReturnListOfDivisibleBy(divisible, input_data)))

