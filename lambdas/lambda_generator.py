#!/usr/bin/python

def Increement(n):
    return lambda x : x+n

x = Increement(5)
print (x(1))
print (x(1))
y = Increement(10)


def MultipleOf5(n):
    return n%5 == 0

filter(MultipleOf5, range(1, 100))
#lambda <return-expression> : <expression/operation>
print(filter(lambda n : n%5==0, range(1, 100)))

print ([n for n in range(1, 100) if n%5== 0])
#[<result> <loop> <conditional-expression>]
