'''
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to 
the nearest leaf node.
Note: A leaf is a node with no children.
Example 1:
    3
   / \
  9  20
    /  \
   15   7
 
Input: root = [3,9,20,null,null,15,7]
Output: 2
Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
In this minimum height between the root and leaf node.
'''
from collections import deque
# Definition for a binary tree node.
class Node(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        level = 0
        q = deque()
        q.append(root)
        while q:
            level += 1
            for _ in range(len(q)):
                node = q.popleft()
                if node.left == None and node.right == None:
                    return level
                if node.left: 
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return 0
    
    def minDepthDFS(self, root):
        if not root:
            return 0
        if not root.left:
            return self.minDepthDFS(root.right) + 1
        if not root.right:
            return self.minDepthDFS(root.left) + 1
        return min(self.minDepthDFS(root.left), self.minDepthDFS(root.right)) + 1

if __name__ =='__main__':
    #  create a Node
    root = Node(4)
    root.left = Node(2)
    root.right = Node(7)
    root.right.left = Node(6)
    root.right.right = Node(9)
    print(Solution().minDepth(root))
    print(Solution().minDepthDFS(root))
