#!/usr/bin/python
import re

def GeneratorGrep(pattern, file_name):
    '''
    Search for a regex pattern in a file
    '''
    fd = open(file_name)
    pat = re.compile(pattern)
    for line in fd:
        if pat.search(line):
            yield line
    fd.close()

def main():
    file_name = input("Enter File Name from which to extract single line comments:")
    comment_line_generator = GeneratorGrep("\A#", file_name)

    for line in comment_line_generator:
        print(line)

if __name__ == "__main__":
    main()
