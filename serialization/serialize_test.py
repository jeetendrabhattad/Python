#!/usr/bin/python

import pickle

fd = open("a.out", "ab")

x = [1,2,3]
y = {"a":1, "b":2}

pickle.dump(x, fd)
pickle.dump(y, fd)

fd.close()

fd = open("a.out", "rb")
try:
    while True:
        print pickle.load(fd)
except EOFError as e:
    pass
