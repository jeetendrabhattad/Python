#!/usr/bin/python

def Enqueue(l1, data):
    l1.append(data)

def Dequeue(l1):
    value = l1[0]
    l1.remove(value)
    return value

def IsEmpty(l1):
    return l1 == []

def Peep(l1):
    return l1[0]

def Menu():
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peep")
    print("4. Display")
    print("5. Exit")
    choice = input("Enter your choice:")
    return choice

def SimulateQueue():
    L1 = []
    while True:
        choice = Menu()
        if choice == 1:
            data = input("Enter Data:-")
            Enqueue(L1, data)
        elif choice == 2:
            if not IsEmpty(L1):
                print("Data is %d"%(Dequeue(L1)))
            else:
                print("List is Empty")
        elif choice == 3:
            if not IsEmpty(L1):
                print("Data at front is %d"%(Peep(L1)))
            else:
                print("List is Empty")
        elif choice == 4:
            print(L1)
        elif choice == 5:
            return

if __name__ == '__main__':
    SimulateQueue()
'''
l2 = []
push(l2,10)
push(l2,11)
push(l2,12)
print pop(l2)
print peep(l2)
print pop(l2)
print pop(l2)
print IsEmpty(l2)
'''
