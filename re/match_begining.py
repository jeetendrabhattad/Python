#!/usr/bin/python

import re

if __name__=="__main__":
    string = "abbcabcdab"
    match = re.match("ab", string)
    if match != None:
        print match.group()
    else:
        print "String not starting with ab"
    
    match = re.search("ab$", "abcdabab")
    if match != None:
        print match.group()
    else:
        print "String not ending with ab"
    
    match = re.search("a.c", "abcdababaxcadc")
    if match != None:
        print match.group()
    else:
        print "a.c not found"
    
    match = re.search("[dab]", "abcdababaxcadc123")
    if match != None:
        print match.group(), match.start(), match.end()
    else:
        print "dab not found"
    
    match = re.search("ab+", "cdababaxcadc123")
    if match != None:
        print match.group(), match.start(), match.end()
    else:
        print "ab not found"
