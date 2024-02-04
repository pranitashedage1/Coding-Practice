# stack can be implemented by using deque from collections module
#  deque is preferred as compared to list as for append and pop it gives O(1) complexity as 
# compared to the list which gives O(n) complexity
# deque is preferred in the list when we need  quicker append and pop operations from both ends of the container

from collections import deque

stack = deque()
stack.append('a')
stack.append('b')
stack.append('c')
print(stack)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack)
