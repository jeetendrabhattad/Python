try:
    r=y
    fd = open("testfile", "r")
    try:
        fd.write("This is test writing !!1")
    finally:
        print("Closing The File")
        fd.close()
except NameError as e:
    print "Except here !!!"
    print e
except IOError as e:
    print "IOError:"
    print e
