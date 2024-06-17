'''
Given the root of a binary tree, return the sum of all left leaves.
A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.

Example 2:
Input: root = [1]
Output: 0
'''
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.sum = 0

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.findSum(root)
        return self.sum
    
    def findSum(self, root):
        if not root:
            return None

        if root.left is not None and root.left.left is None and root.left.right is None:
            self.sum += root.left.val
        
        self.sumOfLeftLeaves(root.left)
        self.sumOfLeftLeaves(root.right)
