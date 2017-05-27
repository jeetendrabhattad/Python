#!/usr/bin/python

fd = open("a.txt")
lines = fd.readlines()

print(map(lambda x : len(x), lines))
fd.close()
