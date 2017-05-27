#!/usr/bin/python

class FileIterator(object):
    def __init__(self, file_name):
        self.fd = open(file_name)
    def __iter__(self):
        return self
    def next(self):
        line = self.fd.readline()
        return line

def main():
    obj = FileIterator(input("Enter FileName:"))
    print(obj.next())
    print(obj.next())
    print(obj.next())
    fileIterator = iter(obj)
    print(type(fileIterator))
    print(next(fileIterator))

if __name__ == "__main__": 
    main()   
