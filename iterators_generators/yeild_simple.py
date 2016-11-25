def Decreement(n):
    for x in n:
        yield x

def Increement(n):
    for x in n:
        #print x
        yield x

def main():
    c = Increement(range(10))
    print(type(c))
    print(next(c))
    print(next(c))
    print(next(c))
    print(next(c))
    print(next(c))
    print(next(c))
    print(next(c))
    print(next(c))
    print(next(c))
    print(next(c))
    #for y in c:
    #    print (y)

if __name__ == "__main__":
    main()
