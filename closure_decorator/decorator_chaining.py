#!/usr/bin/python

import time

def LogDecorator(func):
    def log(args):
        return func(str(time.time())+" "+args)
    return log

def NameDecorator(func):
    def log(args):
        return func("Trinaha Solutions:"+args)
    return log

@LogDecorator
@NameDecorator
def Logger(data):
    print("Logged {}".format(data))

def main():
    Logger("TOP")
    time.sleep(1)
    Logger("PS")

if __name__ == "__main__":
    main()

