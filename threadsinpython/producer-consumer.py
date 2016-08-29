from threading import Thread, Event
import time
data = []
produce_event = Event()
consume_event = Event()

def read():
    global data
    while True:
        if len(data) == 0:
            produce_event.clear()
            produce_event.wait()
        print "\nConsumed ", data[0]
        del data[0]
        consume_event.set()
        time.sleep(1)

def write():
    global data
    while True:
        if len(data) == 10:
            consume_event.clear()
            consume_event.wait()
        val = input("Enter Data:-")
        data.append(val)
        if len(data) == 10:
            produce_event.set()
        time.sleep(0.1)

consumer = Thread(target=read)
producer = Thread(target=write)
consumer.start()
producer.start()

consumer.join()  # Wait for the threads to finish naturally
producer.join()
print "done"
