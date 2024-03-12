# Priority Queue

from queue import PriorityQueue

q = PriorityQueue(maxsize=6)

q.put(56)
q.put(69)
q.put(100)
q.put(4)
q.put(0)
q.put(-6)

print("removing ang getting lowest priority item = ", q.get())
print("removing ang getting lowest priority item = ", q.get())
print("size of the queue = ", q.qsize())
print("is queue empty - ", q.empty())
print("is queue full - ", q.full())
q.put(45)
q.put(53)
print("is queue full - ", q.full())

