'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).
A valid BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:
    2
   / \
  1   3
Input: root = [2,1,3]
Output: true
Example 2:
    5
   / \
  1   4
     / \
    3   6
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4
'''
# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(node, left, right):
            if not node:
                return True
            
            # If values deos not fit in the ranges then return false
            # as tree is not binary search tree
            if not (node.val < right and node.val > left):
                return False
            
            # First call for the left subtree and then right subtree
            # Everything both tree should get satisfied.
            return (valid(node.left, left, node.val) and 
                    valid(node.right, node.val, right))
        
        # First while calling, set left and right values to the infinity.
        return valid(root, float('-inf'), float('inf'))

if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(6)
    print(Solution().isValidBST(root))
