#!/usr/bin/python

import re
def main():
    file_name = input("Enter Input FileName:")
    fd = open(file_name)
    data = fd.read()
    print data
    regex = re.compile("\"\"\"([\w\s]*)\"\"\"")
    for match in regex.finditer(data):
        print(match.start(), match.end())
        print(match.group(1))
    '''
    doc_string = ""
    start_of_comment = False
    end_of_comment = False
    for line in fd:
        Perform Check that the Line read is starting with \'\'\' or \"\"\" (handle spaces)
            if start_of_comment == False:
                start_of_comment = True
                end_of_comment = False
                continue
            else:
                end_of_comment = True
                start_of_comment = False
                print doc_string # add to dictionary as well
                doc_string = ""
        if start_of_comment:
            doc_string += line
    '''    
if __name__ == "__main__":
    main()
