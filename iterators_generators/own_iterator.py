#!/usr/bin/python

class AutoGenerate:
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step
    def next(self):
        self.start += self.step
        if self.start >= self.end:
            raise StopIteration
        return self.start
    def __iter__(self):
        return self

def main():
    x = AutoGenerate(0, 100, 5)
    for y in x:
        print y
    '''z = iter(x)
    print(next(z))
    print(next(z))
    print(next(z))
    '''
if __name__ == "__main__":
    main()
