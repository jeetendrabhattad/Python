import threading
import time
def worker(num):
    """thread worker function"""
    print 'Worker: %s' % num
    time.sleep(num)
    print threading.currentThread().getName()
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,), name="test "+str(i))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
