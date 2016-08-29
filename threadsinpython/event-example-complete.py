from threading import Thread, Event
import time
data = []
size = 0
producer_event = Event()
consumer_event = Event()
#producer_event_network_error = Event()

def read():
    global data
    global size
    global producer_event
    global consumer_event
    print ("Inside consumer ....")
    while True:
        producer_event.wait()
        print "\nConsumed", data[0]
        del data[0] 
        size = size - 1
        consumer_event.set()
        producer_event.clear()

def write():
    global data
    global size
    global producer_event
    print("In producer...")
    while True:
        x = input("Enter Data:-")
        data.append(x)
        size = size + 1
        # add it to queue
        producer_event.set()
        # if queue is full consume.wait()
        if size == 10:
            consumer_event.wait()
            consumer_event.clear()

consumer = Thread(target=read)
producer = Thread(target=write)
consumer.start()
producer.start()

consumer.join()  # Wait for the threads to finish naturally
producer.join()
print "done"
