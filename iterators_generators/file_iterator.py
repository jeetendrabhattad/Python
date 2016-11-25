#!/usr/bin/python

class FileIterator():
    def __init__(self, file_name, decrypt_key):
        self.fd = open(file_name)
        self.decrypt_key = decrypt_key

    def __decrypt(self, line):
        print("Do Decryption {}".format(self.decrypt_key))
        
    def __next__(self):
        """python 3.X needs next to make class iterable"""
        line = self.fd.readline()
        self.__decrypt(line)
        if line == "":
            raise StopIteration
        return line

    def next(self):
        """python 2.7 needs next to make class iterable"""
        return self.__next__()

    def __iter__(self):
        return self

    def __del__(self):
        self.fd.close()

def main():
    file_name = input("Enter file name to read & decrypt:")
    obj = FileIterator(file_name, 5)
    #obj.next()
    obj_iterator = iter(obj)
    
    print(next(obj_iterator)) # 3.X : __next__(obj_iterator)
    print(next(obj_iterator))

if __name__ == "__main__":
    main()
