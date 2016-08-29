import threading
import time
def worker(num):
    """thread worker function"""
    time.sleep(1)
    print 'Worker: %s' % num
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    print("Thread %d Started\n"%i)
#    t.start()
#    t.join()

print("All Threads Started\n")
for x in threads:
    x.start()

for x in threads:
    x.join()

for x in threads:
    print x.isAlive()
print("All Threads Exited\n")
