# Stack can be implemented using LifoQueue
from queue import LifoQueue

stack = LifoQueue(maxsize=3)

print("stack size before adding elements= ", stack.qsize())
#  put will act as a push to add content in the stack
stack.put('a')
stack.put('b')
stack.put('c')
print("stack size after adding elements = ", stack.qsize())
#  if I execute stack.put() on full queue, it will wait untill free slot is available.
# stack.put('e')
# stack.put_nowait() # if I execute this on fill queue, this will raise an exception that queue is full
# stack.put_nowait('d')
#  get will act as pop function to get a content in LIFO order
print("if stack full or not = ", stack.full())   # this method will be removed eventually
print(stack.get())
print(stack.get())
print(stack.get())
#  print stack after removing all values
print("stack size after removing all values", stack.qsize())
print("If stack is empty or not = ", stack.empty()) # this method will be removed eventually
print(stack.get_nowait()) 

