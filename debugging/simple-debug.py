#!/usr/bin/python

import pdb

class Test(object):
    def __init__(self, numberOfIteration):
        self.iterate = numberOfIteration
    def Display(self):
        for i in range(self.iterate):
            pdb.set_trace()
            print (i)
        return

if __name__ == "__main__":
    t = Test(5)
    t.Display()
