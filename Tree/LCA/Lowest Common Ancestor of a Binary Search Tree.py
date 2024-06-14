'''
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between 
two nodes p and q as the lowest node in T that has both p and q as descendants 
(where we allow a node to be a descendant of itself).”

Example 1:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
         6
       /   \
      2     8
     / \   / \
    0   4 7   9
       / \
      3   5
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
         6
       /   \
      2     8
     / \   / \
    0   4 7   9
       / \
      3   5 
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

Example 3:
Input: root = [2,1], p = 2, q = 1
Output: 2
'''
# Time complexity - O(log n)
#  Spcae complexity - O(1)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        while curr:
            # If both p and q are greater than root. go to the right
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            # If both p and q are less than root. go to the left
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            # p is on one side and q on one side, then return root
            else:
                return curr

class Solution1(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if (p.val < root.val and q.val < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        elif(p.val > root.val and q.val > root.val):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root

if __name__ =='__main__':
    #  create a Node
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)

    p = TreeNode(2)
    q = TreeNode(8)

    print(Solution().lowestCommonAncestor(root, p, q))
