#!/usr/bin/python

class Molecule:
    # constructor
    def __init__(self, symbol, atomic_weight):
        print("Constructor")
        self.symbol = symbol
        self.atomic_weight = atomic_weight
        self.__Accumulated = []
        print(id(self.symbol))
    # destructor
    def Buy(self, amount):
        self.__Accumulated.append(amount)
    def __Sell(self):
        print("Private Sell Method")

    def __del__(self):
        print("Destructor")
    # getitem method making object accessible using index like an array
    def __getitem__(self, index):
        '''
            gold = Molecule("AU", 108)
            gold[1] :- gold.__getitem__(1)
        '''
        print("GetItem invoked index = %d"%index)
        return self.__Accumulated[index]
    def getAccumulatedGoldInfo(self, index):
        return self.__Accumulated[index]
    # setitem method making object mutable using index like an array
    def __setitem__(self, index, value):
        print("SetItem invoked index = %d"%index)
    # getslice to make object accessible using slicing syntax
    def __getslice__(self, start, end = 10, step = 1):
        ''' m[2:3]---> m.__getslice__(2,3)'''
        print("start = %d end = %d step = %d"%(start, end, step))
    # call to make object callable like function
    def __call__(self, *args):
        '''
            m(1,2,3)--->m.__call__(1,2,3)
        '''
        print("Using object like function {}".format(args))
    # arithmetic operations
    def __add__(self, obj):
        print("Adding 2 objects")
    
    def __sub__(self, obj):
        print("Subtracting 2 objects")
    
    def __mul__(self, obj):
        print("Multiple 2 objects")
    
    def __div__(self, obj):
        print("Division 2 objects")
    # relational operations
    def __cmp__(self, obj):
        print("Compare 2 objects")
        return 0

def Test2():
    print("Test2 imported\n")
def Test():
    print("Test Not Imported\n")


if __name__ == "__main__":
    m = Molecule("W", 83)
    m[2] = 3
    m[1:2]
    m.Buy(10)
    m.Buy(20)
    m.Buy(5)
    print m[2]
    print m.getAccumulatedGoldInfo(2)
    #print m.__Accumulated[2]
    print m._Molecule__Accumulated[2]
    print dir(m)
    '''
    m[2] = 3
    m[1:2]
    m(1,2,3)
    m+10
    m-10
    m*10
    m/10
    m == m
    x = getattr(m, "symbol") ---> m.symbol
    print (x, id(x))
    print(hasattr(m,"symbol"))
    '''
