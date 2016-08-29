''' This should be used when your function doesnt run but only returns a generator object '''
def CreateGenerator(n):
    mylist = range(n)
    for i in mylist:
         yield i*i

x = CreateGenerator(5)
print(x)
for i in x:
    print(i)

x = CreateGenerator(10)
print(x)
for i in x:
    print(i)
