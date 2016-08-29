def BinarySearch(input_list, search):
    low = 0
    high = len(input_list)

    while low < high:
        mid = (low+high)/2
        print(low, high, mid, input_list[mid])
        if search == input_list[mid]:
            return True
        elif search > input_list[mid]:
            low = mid+1
        else:
            high = mid
    return False

#print(BinarySearch([1,2,3,4,5,6,7,8,9,10], 1))
#print(BinarySearch([1,2,3,4,5,6,7,8,9,10], 10))
print(BinarySearch([1,2,3,4,5,6,7,8,9,10], 5))
print(BinarySearch([1,2,3,4,5,6,7,8,9,10], 15))
'''
def RecBinarySearch(input_list, search):
    low = 0
    high = len(input_list)
    mid = (low+high) / 2
    print(low, high, mid, input_list[mid])

    if search == input_list[mid]:
        return True
    if mid == 0:
        return False

    if search > input_list[mid]:
        return RecBinarySearch(input_list[mid+1:], search)
    else:
        return RecBinarySearch(input_list[:mid], search)

print(RecBinarySearch([1,2,3,4,5,6,7,8,9,10], 1))
print(RecBinarySearch([1,2,3,4,5,6,7,8,9,10], 10))
print(RecBinarySearch([1,2,3,4,5,6,7,8,9,10], 5))
print(RecBinarySearch([1,2,3,4,5,6,7,8,9,10], 15))
'''
