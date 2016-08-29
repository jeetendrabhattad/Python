#!/usr/bin/python

"The food was not that bad, I enjoyed it", "not", "bad", "good"
def ReplaceSequence(input_string, starts_with, ends_with, replace_string):
    """Replaces Sequence with replace string."""
    result = ""
    start_i = input_string.count(starts_with)
    end_i = input_string[input_string.index(starts_with):].count(ends_with)
    if start_i and end_i:
        start_i = input_string.index(starts_with)
        end_i = input_string[start_i:].index(ends_with)+start_i
        result = result + input_string[:start_i]
        result = result + replace_string
        result = result + input_string[end_i+len(ends_with):]
        return result
    return input_string

print(help(ReplaceSequence))

if __name__ == "__main__":
    print(ReplaceSequence("The food was not that bad, I enjoyed it", "not", "bad", "good"))
    print(ReplaceSequence("The food was not that good, I didn't liked it", "not", "good", "bad"))
