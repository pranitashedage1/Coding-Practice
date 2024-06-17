# Balance Binary Tree:
# Time complexity - 
# Auxiliary space - 

'''
Given a binary tree, determine if it is height-balanced.
A height-balanced binary tree is a binary tree in which the depth of the two subtrees of 
every node never differs by more than one.
(Height of left sub tree and right sub tree should not be greater than 1.)
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true

Example 1) - 

        18
       / \
      4  20
         / \
        13 17 
  
    o/p = Yes

Example 2) - 

        10
       / 
      8   
     / 
    6     

    o/p = No

Example 3) - 

        3
       / \
      4   8
     / \   \
    5  9    7
           /
          6

    o/p = No

Example 4) - 

       30
       / \
      40  80
     /  \  /
    50  8  6 
       / \
      20  10

    o/p = Yes

Example 5) - 

        3
       / \
      9  20
         / \
        15  7 
  
    o/p = Yes

   '''
from typing import Optional
class TreeNode:
    def __init__(self, key, left=None, right=None) -> None:
        self.data = key
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:  
        def dfs(root):
            if not root:
                return [True, 0]
            left = dfs(root.left)
            right = dfs(root.right)
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)
            return [balanced, max(left[1], right[1]) + 1]
        return dfs(root)[0]

if __name__ =='__main__':
    #  create a Node
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

# left[0] and right[0] this needs to be add to make sure if nested 
            # subtree is false then in the next iteration, 
            # it will go ahead as false only, To understatn this consider below 
            # example - 
    
    '''
    Example 4:
Input: root = [1,2,2,3,null,null,3,4,null,null,4]
Output: false

         1
       /  \
      2    3
     / \   /\
    3  N  N  3
   / \       /\
  4   N     4  N

    '''