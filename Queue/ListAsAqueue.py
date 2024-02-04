# List can be used as a Queue in Python.
# Instead of enqueue() and dequeue() - append and pop functions can be used.
# However inserting or deleting everything in the beginning takes O(n) time
# as it shifts all the other elements by one.
queue1 = []
queue1.append('a')
queue1.append('b')
queue1.append('c')
print("Initial Queue = ", queue1)
print("elements dequeued from the queue = ")
print(queue1.pop(0))
print(queue1.pop(0))
print(queue1.pop(0))
print("Queue after romoving all elemtnets = ", queue1)
