#!/usr/bin/python

def TurnOffBitPosition(number, bit_position):
    x = 1
    x = x << (bit_position - 1)
    if number & x:
        x = ~x
        return number & x
    return number

def ReplaceSpecificBits(no1, no2, position, bits):
    x = 1
    x = x << bits # 1 << 4 :- 00010000
    x = x - 1 # 00001111
    x = x << (position - bits)
    temp = no2 & x
    no1 = no1 & (~x)
    return no1 | temp


if __name__ =='__main__':
    #number = input("Enter Number:")
    #position = input("Enter Bit Position to turn off:")
    #print(TurnOffBitPosition(number, position))
    print(ReplaceSpecificBits(100, 88, 5, 4))
