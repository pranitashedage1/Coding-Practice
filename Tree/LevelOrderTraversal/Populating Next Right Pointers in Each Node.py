'''
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. 
The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node,
the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.
Example 1:
Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next 
pointer to point to its next right node, just like in Figure B. The serialized output is in level order
as connected by the next pointers, with '#' signifying the end of each level.
Example 2:

Input: root = []
Output: []
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root):
        current = root
        while current is not None:
            itr = current
            while itr is not None:
                # Check if left child is present before connecting
                if itr.left is not None:
                    # Connection between left & right children
                    itr.left.next = itr.right
                
                # Check if itr next & right child is present
                if itr.next is not None and itr.right is not None:
                    # Connection between left & right subtrees
                    itr.right.next = itr.next.left
                
                # Move itr along the level
                itr = itr.next
            current = current.left
        return root

class Solution1(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root is None:
            return None
        q = deque([root])
        while q:
            n = len(q)
            for i in range(n):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                if i == n - 1:
                    node.next = None
                else:
                    node.next = q[0]

        return root
        
