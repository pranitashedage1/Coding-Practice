# Queue is a built-in module of python which is used to implement queue. Maxsize of zero ‘0’ means infinite queue. This follows FIFO rule.
from queue import Queue

q = Queue(maxsize=3)
print("Printing empty Queue - ", q)
print("size of the queue - ", q.qsize())
q.put('a')
q.put('b')
q.put('c')
print("Printing queue - ", q)
print("full = ", q.full())
print("Elements dequeued from the queue")
print(q.get())
print(q.get())
print(q.get())
print("Empty = ", q.empty())
q.put(1)
print("full = ", q.full())
