'''
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).
Example 1:
         1
       /   \
      3     2
     / \      \
    5   3      9

Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]

Example 2:
Input: root = [1,2,3]
Output: [1,3]
'''
from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        q = deque()
        q.append(root)
        result = []
        while q:
            maxValue = float('-inf')
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                maxValue = max(maxValue, node.val)
            result.append(maxValue)
        return result
