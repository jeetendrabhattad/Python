#!/usr/bin/python
import sys
import re
if __name__ =="__main__":
    pattern = input("Enter pattern:-")
    data = input("Enter data in which to search and count occurence of pattern:-")
    original = data
    x = re.search(pattern, data)
    if x == None:
        print("Pattern Not Found\n")
        sys.exit(0)
    count = 1
    while x != None:
        print x.end()
        data = data[x.end():]
        x = re.search(pattern, data)
        if x != None:
            count += 1
    print("Pattern {} found {} times in {}".format(pattern, count, original))
