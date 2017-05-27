#!/usr/bin/python
import sys
import shutil
import argparse

def copyfile(src_file, dest_file, n):
    src_fd = open(src_file)
    dest_fd = open(dest_file, "w")
    if n == 0:
        shutil.copyfileobj(src_fd, dest_fd)
    else:
        line = src_fd.readline()
        while n != 0 and line != "":
            dest_fd.write(line)
            line = src_fd.readline()
            n -= 1
        dest_fd.flush()
    src_fd.close()
    dest_fd.close()
    
def main():
    print(sys.argv)
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", type=str, help="Input/Source File Name")        
    parser.add_argument("-d", type=str, help="Destination File Name")
    parser.add_argument("-n", help="Number of Lines to Copy, default 0(complete file)", action="count", default= 0)
    args = parser.parse_args()

    #copyfile(sys.argv[1], sys.argv[2])
    print args
    copyfile(args.i, args.d, args.n)

if __name__ == "__main__":
    main()
