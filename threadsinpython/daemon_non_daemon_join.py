import threading
import time

def daemon():
    print("Going to sleep\n")
    time.sleep(2) # try with 2 
    print("Wakeup after sleep\n")

def non_daemon():
    print("doing nothing\n")

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)
t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

d.join(3)
print(d.isAlive())
t.join()
