# Stack implementation using LifoQueue

from queue import LifoQueue, Empty

# Create a stack with a maximum capacity of 3 elements
stack = LifoQueue(maxsize=3)

print("Stack size before adding elements =", stack.qsize())

# put() acts as the push operation
stack.put('a')
stack.put('b')
stack.put('c')

print("Stack size after adding elements =", stack.qsize())

# put() blocks if the stack is full until space becomes available.
# Uncommenting the next line will block indefinitely because the stack is full.
# stack.put('d')

# put_nowait() is a non-blocking version of put().
# It raises queue.Full if the stack is already full.
# stack.put_nowait('d')

# full() returns True if the stack has reached its maximum size.
# Note: In multithreaded programs, full() and empty() are only approximate.
print("Is stack full?", stack.full())

# get() acts as the pop operation and removes elements in LIFO order.
print(stack.get())    # c
print(stack.get())    # b
print(stack.get())    # a

print("Stack size after removing all elements =", stack.qsize())

# empty() returns True if the stack is empty.
# Note: In multithreaded programs, this result is only approximate.
print("Is stack empty?", stack.empty())

# get_nowait() is the non-blocking version of get().
# It raises queue.Empty if the stack is empty.
try:
    print(stack.get_nowait())
except Empty:
    print("Cannot pop: Stack is empty.")