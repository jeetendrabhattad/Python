#!/usr/bin/python

'''
class Human
{
    char name[10];
    char address[20];
    public:
    Human(char *n){}
}
'''
class Human:
    address = "INDIA" # class attributes
    count = 0
    def __init__(self, name):
        self.name = name # object attributes
        Human.count = Human.count + 1
        print("Instance count %d"%(Human.count))

    def Walk(self):
        print("Walking: {}".format(self.name))

print Human.address
print Human.__dict__
m1 = Human("mitesh")
print m1.__dict__
j1 = Human("jeetendra")
print j1.__dict__

m1.Walk()
j1.Walk()
