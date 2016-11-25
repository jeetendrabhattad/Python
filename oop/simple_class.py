#!/usr/bin/python
# fd.readline()
class Human:
    planet = "Earth" # class attribute
    # constructor : gets implicitly invoked on object creation
    def __init__(self, age, name):
        print("Constructor")
        self.age = age # object attributes
        self.name = name
        self.type_of_animal = "Social"
        print(id(self.age))
        print(id(Human.planet))
        print(id(self.type_of_animal))
    def __del__(self):
        print("Destructor Invoked {}".format(self.name))
    def Walk(self):
        print("{} is walking".format(self.name))
    def __gt__(self, obj):
        print("gt invoked")
        return self.age > obj.age
def main():
    x = Human(28, "Jeetendra")
    print(x.age)
    print(x.name)
    #x[1:2:1]
    y = Human(30, "Bharat")
    print(y.age)
    print(y.name)

    x.Walk()
    y.Walk()

    x.teach = True

    print (x.__dict__)
    print (y.__dict__)
    print (dir(x))

    x > y # x.__gt__(y)
if __name__ == "__main__":
    main()
'''
    Human.planet = "Jupiter"
    print (x.planet)
    print (y.planet)
    print x.__dict__
    print (dir(x))
    print (dir(y))
    #print (dir(Human))
'''
