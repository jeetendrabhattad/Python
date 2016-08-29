#!/usr/bin/python

def GenerateString(input_string):
    output_string = ""
    i = 0
    while i < len(input_string):
        count = 1
        char_to_check = input_string[i]
        print char_to_check
        while i+1 != len(input_string) and char_to_check == input_string[i+1]:
        #char_to_check == input_string[i+1] and i+1 != len(input_string): if u check data first and then length it will result into an IndexError exception
            count += 1
            i += 1
        output_string += char_to_check
        output_string += str(count)
        i += 1
    return output_string

if __name__ == "__main__":
    input_string = input("Enter string:-")
    output_string = GenerateString(input_string)
    print("Output string is {} for input string {}".format(output_string, input_string))
