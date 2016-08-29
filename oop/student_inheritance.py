#!/usr/bin/python

class Person:
    def __init__(self, name, address, age):
        self.name = name
        self.address = address
        self.age = age
    def __str__(self):
        return "Name:"+self.name+" Address:"+self.address+" Age:"+str(self.age)

class Student(Person):
    roll_no = 0
    def __init__(self, name, address, age, div, marks):
        '''
        attributes = {}
        attributes["name"] = name
        attributes["address"] = address
        attributes["age"] = age
        '''
        #apply(Person.__init__, (self,), attributes)
        Person.__init__(self, name, address, age)

        #super(Student, self).__init__(name, address, age)
        self.div = div
        Student.roll_no += 1
        self.rollNo = Student.roll_no
        self.marks = marks
    def __str__(self):
        #return apply(Person.__str__, (self,))+" RollNo:"+str(self.rollNo)
        #return super(Student, self).__str__()+" RollNo:"+str(self.rollNo)
        return Person.__str__(self)+" RollNo:"+str(self.rollNo)


if __name__ == '__main__':
    x = Student("Jeetendra", "Pune", 28, "A", [97,97,97])
    y = Student("Jeetendra", "Pune", 28, "A", [97,97,97])
    print (x)
    print (y)
    print (y.__dict__)
