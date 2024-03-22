'''
Given the root of a binary search tree, and an integer k, 
return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Example 1:
    3
   / \
  1   4
   \
    2
Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:
        4
       / \
      3   6
     / \
    2   4
   /
  1    

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
'''
# Time complexity: O(H+k), where H is a tree height. 
# This complexity is defined by the stack, which contains at least H+k elements, 
# since before starting to pop out one has to go down to a leaf. 
# This results in O(log⁡N+k)for the balanced tree and 
# O(N+k)for a completely unbalanced tree with all the nodes in the left subtree.

# Space complexity: O(H) to keep the stack, where H is a tree height. 
# That makes O(N)in the worst case of the skewed tree, 
# and O(log⁡N)in the average case of the balanced tree.

# This can also be solved with the help of inorder traveral, First create a 
# list wiht inorder traversal then find the (k-1) index.
# In this we have solved with iteratinve, stack method
# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right

if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)
    print(Solution().kthSmallest(root, 3))
