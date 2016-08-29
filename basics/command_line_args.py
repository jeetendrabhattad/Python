#!/usr/bin/python

import sys

#def DisplayFileContents(
if __name__ == '__main__':
    print len(sys.argv)
    print type(sys.argv)
    fcount = sys.argv.count('-f')
    findex = 0
    print "Files"
    for _ in range(fcount):
        if sys.argv[findex:].__contains__('-f'):
            findex = findex+sys.argv[findex:].index('-f') + 1
            print sys.argv[findex]
            #DisplayFileContents(sys.argv[findex])
    dindex = 0
    print "Directories"
    dcount = sys.argv.count('-d')
    for _ in range(dcount):
        if sys.argv[dindex:].__contains__('-d'):
            dindex = dindex + sys.argv[dindex:].index('-d') + 1
            print sys.argv[dindex]

