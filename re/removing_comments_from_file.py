#!/usr/bin/python

import re
import tempfile

def main():
    file_name = input("Enter filename from which to remove comments:")
    file_handle = open(file_name)
    line = file_handle.readline()
    temp_file = tempfile.NamedTemporaryFile()

    while line != "":
        match = re.search("#", line)
        if match:
            if match.start() != 0:
                temp_file.write(line[0:match.start()])
                temp_file.write("\n")
        else:
            temp_file.write(line)
        line = file_handle.readline()
    file_handle.close()
    temp_file.seek(0, 0)
    
    file_handle = open(file_name, "w")
    line = temp_file.readline()
    while line != "":
        if "\n" not in line[0]:
            file_handle.write(line)
        line = temp_file.readline()

    file_handle.close()
    temp_file.close()

if __name__ == "__main__":
    main()
