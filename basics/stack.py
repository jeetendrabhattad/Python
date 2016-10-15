#!/usr/bin/python

def Push(l1, data):
    l1.append(data)

def Pop(l1):
    return l1.pop()

def IsEmpty(l1):
    return l1 == []

def IsFull(l1):
    return len(l1) == 10
    
def Peep(l1):
    return l1[-1]

def Menu():
    print("1. Push")
    print("2. Pop")
    print("3. Peep")
    print("4. Display")
    print("5. Exit")
    choice = input("Enter your choice:")
    return choice

def SimulateStack():
    L1 = []
    while True:
        choice = Menu()
        if choice == 1:
            data = input("Enter Data:-")
            if not IsFull(L1):
                Push(L1, data)
            else:
                print("Stack is full pop something")
        elif choice == 2:
            if not IsEmpty(L1):
                print("Data is %d"%(Pop(L1)))
            else:
                print("Stack is Empty")
        elif choice == 3:
            if not IsEmpty(L1):
                print("Data at top is %d"%(Peep(L1)))
            else:
                print("Stack is Empty")
        elif choice == 4:
            print(L1)
        elif choice == 5:
            return

if __name__ == '__main__':
    SimulateStack()
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
