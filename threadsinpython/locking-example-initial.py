from threading import Thread
from threading import Lock
import time

threads = []
data = 0
lock = Lock()

def get_job():
    global data
    lock.acquire()
    data += 1
    time.sleep(0.1)
    x = data
    lock.release()
    return data

def process_job():
    print get_job()
#    global data
#    print data

for i in range(10):
    thread = Thread(target=process_job)
    #thread = Thread(target=get_job)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
