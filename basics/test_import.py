#!/usr/bin/python

import max3
import collections
queue = collections.deque((10,20,30))
#max3.max3(10, 20, 30)
print queue
queue.pop()
print queue
queue.popleft()
print queue
