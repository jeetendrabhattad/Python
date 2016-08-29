#!/usr/bin/python

class Complex:
    def __init__(self, real=0, imag=0):
        ''' Constructor '''
        print("Init invoked for "+str(id(self)))
        self.iReal = real
        self.iImag = imag
    def Add(self, real):
        ''' Adds to real part of Complex number '''
        self.iReal += real
        self.Result = 10
    def Display(self):
        ''' Display's Complex Number '''
        print("Complex number is: %d+%di"%(self.iReal, self.iImag))

if __name__=="__main__":
    c1 = Complex(10, 20)
    print(id(c1))
    c1.Display()
    c2 = Complex(12, 24)
    c3 = Complex(1,2)
    c2.Display()
    c3.Add(10)
    c3.Display()

    c4 = Complex()
