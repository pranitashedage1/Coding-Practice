'''
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical,
and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]

  1              
 / \       
2   3

  1              
 / \       
2   3
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
  1
 /
2  

1
 \
  2
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
  1              
 / \       
2   1

  1              
 / \       
1   2
Output: false
'''
# Time complexity - O(p + q)
from typing import Optional
class TreeNode:
    def __init__(self, key, left=None, right=None) -> None:
        self.val = key
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both tree are not empty then return True.Means both tree are same
        if not p and not q:
            return True
        # If  either of tree emepty then return False
        # Or if both nodes are non empty In this case, now compare their values
        if not p or not q or p.val != q.val :
            return False

        # Now recursively call subtrees
        return (self.isSameTree(p.left, q.left) and 
        self.isSameTree(p.right, q.right))

if __name__ =='__main__':
    #  create a Node
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root1 = TreeNode(3)
    root1.left = TreeNode(1)
    root1.right = TreeNode(20)

print(Solution().isSameTree(root, root1))