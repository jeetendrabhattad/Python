import threading
import time

def daemon():
    while True:
        print("Going to sleep\n")
        time.sleep(1)
        print("Wakeup after sleep\n")

def non_daemon():
    time.sleep(5)
    print("doing nothing\n")

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)
t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()
#while True:
#    time.sleep(2)
t.join(3)
print t.isAlive()
#d.join()
