#!/usr/bin/python

def Add2Numbers(self):
    return self.no1+self.no2

def Mul(self):
    return self.no1*self.no2

def init(self, a, b):
    self.no1 = a
    self.no2 = b

def main():
    Arithmetic = type('Arithmetic', (object,), {'__init__':init, 'Adding':Add2Numbers, 'Mul':Mul})
    obj = Arithmetic(10, 20)
    print(obj.Adding())
    print(obj.Mul())

if __name__ == "__main__":
    main()
