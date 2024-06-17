'''
Given the root node of a binary search tree and two integers low and high, 
return the sum of values of all nodes with a value in the inclusive range [low, high].
Example 1:
Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.

Example 2:
Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.
'''
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        def dfs(node):
            nonlocal ans
            if node:
                if low <= node.val <= high:
                    ans += node.val
                if low < node.val:
                    dfs(node.left)
                if node.val < high:
                    dfs(node.right)
        ans = 0
        dfs(root)
        return ans


class Solution1:
    def __init__(self):
        self.sum = 0

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return
        self.rangeSum(root, low, high)
        return self.sum

    def rangeSum(self, root, L, R):
        if not root:
            return 
        
        if root.left:
            self.rangeSum(root.left, L, R)
        
        if root.val >= L and root.val <= R:
            self.sum += root.val
        
        if root.right:
            self.rangeSum(root.right, L, R)
