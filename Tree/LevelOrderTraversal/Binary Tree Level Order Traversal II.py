'''
Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).

 

Example 1:
         3
       /   \
      9     20
            / \
           15  7

Input: root = [3,9,20,null,null,15,7]
Output: [[15,7],[9,20],[3]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
'''
from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q = deque()
        q.append(root)
        result = []
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    level.append(node.val)
            if level:
                result.insert(0, level)
        return result
