'''
Given the root of a binary tree with unique values and the values of two different nodes 
of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are cousins,
 or false otherwise.

Two nodes of a binary tree are cousins if they have the same depth 
with different parents.

Note that in a binary tree, the root node is at the depth 0, and 
children of each depth k node are at the depth k + 1.

Example 1:
Input: root = [1,2,3,4], x = 4, y = 3
Output: false

Example 2:
Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true

Example 3:
Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false
'''
from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        if not root:
            return False
        
        q = deque([root])
        
        while q:
            size = len(q)
            isA = isB = False

            for _ in range(size):
                node = q.popleft()
                if node.val == x:
                    isA = True
                if node.val == y:
                    isB = True
                if isA and isB:
                    return True
                
                if node.left and node.right:
                    if (node.left.val == x and node.right.val == y) or (node.left.val == y and node.right.val == x):
                        return False

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            if isA and isB:
                return True
            if isA or isB:
                return False
        return False

