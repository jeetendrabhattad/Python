#!/usr/bin/python

def CountConsonants(string):
    count = 0
    string = string.upper()
    for x in string:
        if x not in ["A", "E", "I", "O", "U"]:
        #if x == "A" or x == "E" or x == "I" or x == "O" or x == "U":
        #    pass
        #else:
            count += 1
    return count

if __name__ == "__main__":
    string = input("Enter string of which to count consonants:")
    print("Number of consonants in given string %s are %d"%(string, CountConsonants(string)))
