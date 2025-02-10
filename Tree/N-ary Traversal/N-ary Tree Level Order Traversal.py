"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""
from collections import deque

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return
        output = []
        queue = deque()
        queue.append(root)
        while queue:
            n = len(queue)
            temp = []
            for i in range(n):
                node = queue.popleft()
                if node:
                    temp.append(node.val)
                    queue.extend(node.children)
            output.append(temp)
        
        return output

