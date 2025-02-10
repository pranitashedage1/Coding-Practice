"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""
from collections import deque

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return
        self.result = []
        self.helper(root)
        return self.result


    def helper(self, root):
        if not root:
            return
        for child in root.children:
            self.helper(child)
        self.result.append(root.val)
