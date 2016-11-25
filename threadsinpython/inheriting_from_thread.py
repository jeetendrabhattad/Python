import threading

class SubThread(threading.Thread):

    def run(self):
        print("Running......\n")
        return


for i in range(5):
    t = SubThread()
    t.start()
