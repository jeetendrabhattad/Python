import threading
import time
def worker(num):
    """thread worker function"""
    time.sleep(1)
    print threading.currentThread().getName()
    print 'Worker: %s' % num

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,), name="t"+str(i))
    threads.append(t)
    print("Thread %d Started\n"%i)
#    t.start()
#    t.join()

for y,x in enumerate(threads):
    if(y==2):
        x.setDaemon(True);
print("All Threads Started\n")
for x in threads:
    x.start()
for x in threads:
    print x.isAlive(), x.isDaemon()
print("Main Done\n")
