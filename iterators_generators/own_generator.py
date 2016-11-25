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
        yield self.start
    def __iter__(self):
        return self
def main():
    x = AutoGenerate(0, 100, 5)
    print(type(x))
    z = iter(x)
    for y in x:
        print y
    print(next(z))
    print(next(z))
    print(next(z))
    print(help(z))

if __name__ == "__main__":
    main()
