'''
Within a binary tree, a node x is considered good if the path from the root of the tree to the node x contains no nodes with a value greater than the value of node x

Given the root of a binary tree root, return the number of good nodes within the tree.

Example 1:
Input: root = [2,1,1,3,null,1,5]
                2
              /   \
            1       1
          /        /  \
        3         1    5
Good nodes are 3, 2, 5
Output: 3

Example 2:
Input: root = [1,2,-1,3,4]

                1
              /   \
            2      -1
          /   \     
        3      4   
good nodes are 1, 2, 3, 4
Output: 4
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        maxVal = float('-inf')
        def dfs(node, maxVal):
            nonlocal count
            if not node:
                return
            if maxVal <= node.val:
                count += 1
                maxVal = node.val
            dfs(node.left, maxVal)
            dfs(node.right, maxVal)
        
        dfs(root, maxVal)
        return count
