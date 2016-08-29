#!/usr/bin/python
import math

def CalcRectangle(length):
    sqrt = math.sqrt(length)
    x = math.floor(sqrt)
    y = math.ceil(sqrt)
    if x*y < length:
        x = y
    return x, y

def JumbleLetters(input_message, breadth):
    output_message=""
    i = 0
    count = 0
    length = len(input_message)
    while count < length:
        j = i;
        while j < length:
            output_message += input_message[j]
            j += breadth
            count += 1
        #output_message+='\n'
        i += 1
    #print output_message
    return output_message

def ComposeSecretMessage():
	input_message = input("Please Enter String:-")
	print input_message
	input_message = input_message.replace(' ','')
	print input_message
	length, breadth = CalcRectangle(len(input_message))
	print length, breadth
	jumble_string = JumbleLetters(input_message, int(length))
    #print jumble_string

if __name__ == '__main__':
	ComposeSecretMessage()		
