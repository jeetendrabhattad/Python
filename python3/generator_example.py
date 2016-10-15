''' This should be used when your function doesnt run but only returns a generator object '''
def CreateGenerator(n):
    def inner():
        for i in range(n):
            yield i*i
    return inner

x = CreateGenerator(5)
for y in x():
    print y
'''
print(x)
for i in x:
    print(i)
    break
'''
