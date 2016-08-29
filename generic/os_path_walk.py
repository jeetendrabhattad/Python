import os
import sys

c_count = 0
cpp_count = 0
py_count = 0
h_count = 0
other_count = 0
def callback(arg, directory, files):
    global c_count
    global cpp_count
    global py_count
    global h_count
    global other_count
    for file1 in files:
        #print os.path.join(directory, file1)#, repr(arg)
        if file1.endswith(".py"):
            py_count += 1
        elif file1.endswith(".c"):
            c_count += 1
        elif file1.endswith(".cpp"):
            cpp_count += 1
        elif file1.endswith(".h"):
            h_count += 1
        else:
            other_count += 1

print sys.argv
os.path.walk("/home/jeetendra/Documents/Personal/python_practice/generic/", callback, "directory traverse")
print py_count, c_count, cpp_count, h_count, other_count
