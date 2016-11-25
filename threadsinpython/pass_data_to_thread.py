#!/usr/bin/python

import threading
import time

data = 10
lock = threading.Lock()

def ThreadFunction(args):
    print threading.currentThread().getName() 
    global data
    lock.acquire()
    data += 1
    #time.sleep(0.1) # some more stuff
    y = data
    #print(args)
    #print(data)
    #print threading.currentThread().getName()
    lock.release()
    return y

def Calculate():
    print("Calculate Executed.")

def ThreadWrapper(args):
    #...
    Calculate()
    x = ThreadFunction(args)
    print x
    #...
def main():
    thread = []
    for i in range(5):
        t1 = threading.Thread(target=ThreadWrapper, args=(["Hello"]), name = "thread "+str(i))
        thread.append(t1)
        t1.start() # thread starts
        #t1.join() # wait until thread terminates
    for x in thread:
        x.join()

if __name__ == "__main__":
    main()


'''
fd = socket
queue = []
while True:
    data = fd.read()
    queue.append(data)
    Notify
'''

'''
    Process(data)
'''
