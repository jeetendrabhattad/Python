#!/usr/bin/python

import time

def LogDecorator(func):
    def log(args):
        return func(str(time.time())+" "+args)
    return log

@LogDecorator
def Logger(data):
    print("Logged {}".format(data))

Logger("Thanks it is now easy to understand...")
'''
x = LogDecorator(Logger)
x("Hello This is Difficult to Digest")
'''
'''
def SimpleLog(data):
    return str(time.time())+" "+data

def ErrorLog(data):
    return str(time.time())+" "+data

def main():
    print(SimpleLog("TOP"))
    time.sleep(1)
    print(SimpleLog("PS"))

if __name__ == "__main__":
    main()
'''
