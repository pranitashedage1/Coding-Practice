# Calculate maximum height of the tree.
#  Time Complexity - O(n)
#  Auxiliary Space  - O(h)
# Binary Tree Implementation:
'''
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node 
down to the farthest leaf node.

        4
       / \
      2   7
         / \
        6   9
o/p = 3
         
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2
'''
from collections import deque

# Definition for a binary tree node.
class Node(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        maxHeight = max(left, right) + 1
        return maxHeight

    def maxDepthBFA(self, root):
        if not root:
            return 0
        level = 0
        q = deque()
        q.append(root)
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level

if __name__ =='__main__':
    #  create a Node
    root = Node(4)
    root.left = Node(2)
    root.right = Node(7)
    root.right.left = Node(6)
    root.right.right = Node(9)
    print(Solution().maxDepth(root))
    print(Solution().maxDepthBFA(root))
