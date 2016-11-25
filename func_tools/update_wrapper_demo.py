import functools

def add(a, b=2):
    '''simple add function'''
    return a+b

p1 = functools.partial(add, b = 4)
functools.update_wrapper(p1, add)
print(p1(10))
print(p1.__doc__)
#print(p1()) #TypeError: add() takes at least 1 argument (1 given)
