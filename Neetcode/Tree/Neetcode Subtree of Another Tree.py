'''
Given the roots of two binary trees root and subRoot, 
return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants.
The tree tree could also be considered as a subtree of itself.
Example 1:
Input: root = [3,4,5,1,2], subRoot = [4,1,2]

        3
       / \
      4   5
     / \    
    1   2  

      4   
     / \    
    1   2
Output: true

Example 2:
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
        3
       / \
      4   5
     / \    
    1   2
       /
      0 

      4 
     / \    
    1   2
Output: false
'''
# Time complexity - O(s * t)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # If subtree is null and there is s tree, then return True
        if not subRoot:
            return True
        # If above if does not execute means t not empyt and 
        # now we will check s, If s is null then return True
        if not root:
            return False

        
        # if control comes here means ther s and t and we will check if subtree is in 
        # the tree, it it return true
        if self.sameTree(root, subRoot):
            return True
        # If control comes here means it did not work for the parent tree, call it 
        # for left subtee and right subtree
        return (self.isSubtree(root.left, subRoot) or
                 self.isSubtree(root.right, subRoot))

    def sameTree(self, root, subRoot):
        # if both tree are null, then return True
        if not root and not subRoot:
            return True
        
        if root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.left, subRoot.left) and 
            self.sameTree(root.right, subRoot.right))

if __name__ =='__main__':
    #  create a Node
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)
    root1 = TreeNode(4)
    root1.left = TreeNode(1)
    root1.right = TreeNode(2)
    # Input: root = [3,4,5,1,2], subRoot = [4,1,2]
    print(Solution().isSubtree(root, root1))
