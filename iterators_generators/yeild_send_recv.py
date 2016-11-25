import random

def consume():
    while True:
        data = yield
        print("Received : {}".format(data))

def produce(consumer):
    while True:
        data = random.randint(1, 1000)
        consumer.send(data)
        yield

if __name__ == '__main__':
    consumer = consume()
    consumer.send(None)
    producer = produce(consumer)

    for _ in range(20):
        next(producer)
