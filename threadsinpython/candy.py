#!/usr/bin/env python
from atexit import register
from random import randrange
from threading import BoundedSemaphore, Lock, Thread
from time import sleep, ctime

lock = Lock()
MAX = 10
candytray = BoundedSemaphore(MAX)
def refill():
	lock.acquire()
	print 'Refilling candy...',
        print candytray._Semaphore__value
	try:
		candytray.release()
        except ValueError:
	        print 'full, skipping'
	else:
		print 'OK'
	lock.release()

def buy():
         lock.acquire()
         print 'Buying candy...',
         print candytray._Semaphore__value
         if candytray.acquire(False):
             print 'OK'
         else:
             print 'empty, skipping'
         lock.release()
 
def producer(loops):
         #for i in xrange(loops):
         while True:
             refill()
             sleep(randrange(3))
  
def consumer(loops):
#         print loops, type(xrange(loops))
         for i in xrange(loops):
#         while True:
#             print type(i)
             buy()
             sleep(randrange(3))
  
def _main():
         print 'starting at:', ctime()
         nloops = 5
         print nloops
         print 'THE CANDY MACHINE (full with %d bars)!' % MAX
         Thread(target=consumer, args=(nloops+2,)).start() # buyer
         Thread(target=producer, args=(nloops,)).start() #vndr
#decorator
#@atexit.register
#def cleanup():
#    pass
@register
def _atexit():
         print 'all DONE at:', ctime()
 
if __name__ == '__main__':
         _main()
