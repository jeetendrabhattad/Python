#!/usr/bin/python

def from_keys(input_dict, input_values):
    # if not type(input_dict) is dict:
    if not isinstance(input_dict, dict):
        return "input_dict is not dictionary"
    result_dict = {}
    index = 0
    length = len(input_values)
    for x in input_dict:
        #data = None
        if(index < length):
        #data = input_values[index]
            result_dict[x] = input_values[index]
            index += 1
        else:
            result_dict[x] = None
    return result_dict

def main():
    input_dict = {1:"a", 2:"b", 3:"c",4:"d"} 
    input_values = [1,2,3]
    result = from_keys(input_dict, input_values)
    print result

if __name__ == "__main__":
    main()
