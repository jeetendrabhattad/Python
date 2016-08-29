#!/usr/bin/python

def MergeLists(L1, L2):
    i = 0
    j = 0
    L3 = []
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            L3.append(L1[i])
            i += 1
        else:
            L3.append(L2[j])
            j += 1
    
    if i < len(L1):
        L3.extend(L1[i:])
    if j < len(L2):
        L3.extend(L2[j:])

    return L3
if __name__ == '__main__':
    l1 = list(input("Enter List1:"))
    l2 = list(input("Enter List2:"))
    l1.sort()
    l2.sort()
    print("l1 is {}\n l2 is {}\n Merge Result is {}".format(l1, l2, MergeLists(l1,l2)))

