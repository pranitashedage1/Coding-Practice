'''
Given the root of a binary tree and an integer targetSum, return true if the tree has a 
root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.

Example 2:
Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.

Example 3:
Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        return self.path_sum(root, sum)

    def path_sum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        # We need to subtract root.val while comparing also because in the next
        # recursive call when the sum is equal to 0 it won't reach this
        # statement since we return false if root is None
        if not root.left and not root.right and sum - root.val == 0:
            return True
        left = self.path_sum(root.left, sum - root.val)
        right = self.path_sum(root.right, sum - root.val)
        return left or right
