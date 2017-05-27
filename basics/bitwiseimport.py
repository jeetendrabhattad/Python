#!/usr/bin/python

def ReplaceBits(x, y, position, noOfBits):
	'''Example	
		x = 256 100000000
		y = 63  000111111
		pos = 3
		noOfBits = 3
	'''
	temp = 2**noOfBits-1
	temp = temp<<(position - noOfBits)
	y = y&temp
	x = x&~temp
	return x|y

def TurnOffRightMostBit(no):
	return no & (no-1)

def DivisionByTwoPower(n,power):
	res=n>>power
	return res

def ToggleBit(n,pos):
	x=1<<(pos-1)
	result=n^x
	return result

def IsDivisibleByEight(n):
	result = n & 7
	if result == 0:
		return True 
	return False
		
def TurnOn(n,pos):
	#y=1<<(pos-1)
    y = 2**(pos-1)
    result=n|y
    return result

def TurnOff(n,pos):
	y=~(1<<(pos-1))
    #y= ~(2**(pos-1))
	result=n&y
	return result

def TurnOffSetOfBits(number, pos, noOfBits):
    x = 2**noOfBits - 1
    x = x << (pos - noOfBits)
    x = ~x
    return number & x

def TurnOnSetOfBits(number, pos, noOfBits):
    x = 2**noOfBits - 1
    x = x << (pos - noOfBits)
    return number | x

def ToggleSetOfBits(number, pos, noOfBits):
    x = 2**noOfBits - 1
    x = x << (pos - noOfBits)
    return number ^ x

def MultiplicationByTwo(n,power):
	res=n<<power
	return res

def CountNoOfOneBits(n):
    x = 1
    count = 0
    print(bin(n))
    while True:
        if x & n:
            count += 1
        x = x << 1
        print (x)
        if x == 2**64:
            break
    return count

if __name__ == '__main__':
	#number = input("Enter Number to check divisbility by 8:")
	#print("T/F {} is divisible by 8:- {}".format(number, IsDivisibleByEight(number)))
	x = input("Enter x:")
	#y = input("Enter y:")
	#pos = input("Enter position:")
	#noOfBits = input("Enter Number of Bits:")
	print(CountNoOfOneBits(x))
