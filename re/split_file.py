fd = open("multiple_patterns.py","r")
for line in  fd.readlines():
    l1 = line.split("#")
    try:
        print l1[1]
    except:
        pass
