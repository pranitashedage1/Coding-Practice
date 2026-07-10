# i) Stack can be implemented by using deque from collections module

# ii) deque and list both provide O(1) append() and pop() operations at the right end. 
# deque is preferred only when insertions and deletions are required from both ends because appendleft() and popleft() are also O(1), whereas list.insert(0) and list.pop(0) are O(n).

# iii) deque is preferred in the list when we need  quicker append and pop operations from both ends of the container


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
