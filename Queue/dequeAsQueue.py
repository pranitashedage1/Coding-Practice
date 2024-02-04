# i) Deque is preferred over list in the cases where we need quicker append and pop operations from both ends of the container. 
# ii) As deque provides  O(1) of time complexity for append and pop operations from both ends of the container as compared to list which provides O(n) time complexity.
# iii) Instead of dequeue and enqueue, append() and popleft() functions are used.

from collections import deque
q = deque()
q.append('a')
q.append('b')
q.append('c')
print("Initial queue")
print(q)
print(q.popleft())
print(q.popleft())
print(q.popleft())
print("After removing elements")
print(q)
