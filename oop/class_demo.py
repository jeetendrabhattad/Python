class Complex:
    '''
        Complex class demonstration
    '''
    def __init__(self, realpart = 0, imagpart = 0):
        '''
            c = Complex(10, 20)
            c = Complex()
            c = Complex(10)
        '''
        print 'Calling constructor'
        self.real = realpart
        self.imag = imagpart

    def __del__(self):
        print 'Calling Destructor'

    def __str__(self):
        '''
            to display object using print method
        '''
        print("Converting object to string")
        return str(self.real)+" "+str(self.imag)+"i"    

    def add(self, c2):
        '''
            c1 = Complex(1,2)
            c2 = Complex(3,2)
            c3 = c1.add(c2) c1 goes as 1st argument & c2 as second. i.e c1 is calling object and defacto name is self
            # c1+c2:c1.__add__(c2)
        '''
        print ("adding ")
        return Complex(self.real+c2.real, self.imag+c2.imag)

    def __add__(self, c2):
        # c1 + c2: c1.__add__(c2) : Complex.__add__(c1, c2)
        print ("adding+++++ ")
        c3 = Complex(self.real +c2.real, self.imag+c2.imag)
        return c3
        #return Complex(self.real+c2.real, self.imag+c2.imag)

    def __sub__(self, c2):
        print("Subtraction of complex needs to be defined")
        return Complex(self.real-c2.real, self.imag-c2.imag)

    def __eq__(self, c2):
        return self.real == c2.real and self.imag == c2.imag

    def __mul__(self, mul):
        return Complex(self.real*mul, self.imag)

def Menu():
    print("*****Complex Number Operations******")
    print("\n1.Add\n2.Subtract\n3.Multiply\n4.Compare\n5.Exit")
    choice = input("Enter your choice:")
    return choice

def main():
    choice = Menu()
    while(choice != 5):
        if choice == 1:
            print("call add")
            r = input("Enter real part:")
            i = input("Enter imaginary part:")
            c1 = Complex(r, i)
            r = input("Enter real part:")
            i = input("Enter imaginary part:")
            c2 = Complex(r, i)
            c3 = c1 + c2
            print c1
            print c2
            print c3
        elif choice == 2:
            print("call subtract")
        elif choice == 3:
            print("call multiply")
        elif choice == 4:
            print("call compare")
        choice = Menu()

if __name__ == "__main__":
    main()
'''
x = Complex(3.0, -4.5)

y = Complex(1, 4)
print x.real, x.imag
print x # x.__str__() implicilty invoked 
#print x.__str__()
w = x+y
print w
w = x-y
'''
'''
z=x.add(y)
print w
print z
print x.__dict__
print y.__dict__
print Complex.__dict__
'''
