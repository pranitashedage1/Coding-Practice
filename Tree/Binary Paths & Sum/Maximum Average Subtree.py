'''
Given the root of a binary tree, return the maximum average value of a subtree of that tree. 
Answers within 10-5 of the actual answer will be accepted.
A subtree of a tree is any node of that tree plus all its descendants.
The average value of a tree is the sum of its values, divided by the number of nodes.

Example 1:
Input: root = [5,6,1]
Output: 6.00000
Explanation: 
For the node with value = 5 we have an average of (5 + 6 + 1) / 3 = 4.
For the node with value = 6 we have an average of 6 / 1 = 6.
For the node with value = 1 we have an average of 1 / 1 = 1.
So the answer is 6 which is the maximum.

Example 2:
Input: root = [0,null,1]
Output: 1.00000
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
        self.max = float('-inf')

    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        self.maxAvg(root)
        return self.max

    def maxAvg(self, root):
        if root is None:
            return [0, 0]

        left = self.maxAvg(root.left)
        right = self.maxAvg(root.right)

        current_sum = left[0] + right[0] + root.val
        current_count = left[1] + right[1] + 1

        current_avg = current_sum/current_count
        self.max = max(self.max, current_avg)

        return [current_sum, current_count]
