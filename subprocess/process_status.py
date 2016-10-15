#!/usr/bin/python

import subprocess
import time

def StartProcessStatus(timeout):
    count = 0
    while count != 10:
        output = subprocess.check_output(["top"])
        print output
        count += 1
        time.sleep(timeout)

if __name__ == "__main__":
    timeout = input("Enter Periodic Time after which ps output is to be displayed:")
    StartProcessStatus(timeout)
