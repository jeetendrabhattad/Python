#!/usr/bin/python

import time

def LogDecorator(func):
    def log(args):
        return func(str(time.time())+" "+args)
    return log

def NameDecorator(func):
    def log(args):
        return func("Stellus:"+args)
    return log

#Logged Stellus:1477370315.59 TOP
#Logged 1477370315.59 TOP
@LogDecorator
#Logged Stellus: TOP
@NameDecorator
# stellus timing top
# timing top -- > stellus timing top
#x = LogDecorator(Logger)
#x(data)
def Logger(data):
    print("Logged {}".format(data))


def main():
    Logger("TOP")
    time.sleep(1)
    Logger("PS")

if __name__ == "__main__":
    main()

