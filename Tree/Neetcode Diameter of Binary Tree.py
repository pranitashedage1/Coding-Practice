#  Time Complexity - O(n)
# Binary Tree Implementation:
'''
Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.

        4
       / \
      2   7
         / \
        6   9
o/p = 3   as longest path will be [2-4-7-9] or [2-4-7-6]
 
Example 1:
Input: root = [1,2,3,4,5]
        1
       / \
      2   3
     / \    
    4   5    
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:
Input: root = [1,2]
Output: 1
'''
from queue import Queue
class Node:
    def __init__(self, key, left=None, right=None) -> None:
        self.data = key
        self.left = left
        self.right = right

def printheight(root):
    if not root:
        return 0
    left = printheight(root.left)
    right = printheight(root.right)
    height = max(left, right) + 1
    return height

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        diameter = 0

        def dfs(node):
            if node == None:
                return 0
            nonlocal diameter
            # recursively find the longest path in
            # both left child and right child
            left = dfs(node.left)
            right = dfs(node.right)
            # update the diameter if left_path plus right_path is larger
            diameter = max(diameter, left + right) 
            # return the longest one between left_path and right_path;
            # remember to add 1 for the path connecting the node and its parent
            return max(left, right) + 1   
        dfs(root)
        return diameter


if __name__ =='__main__':
    #  create a Node
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    # print(printheight(root))
    print(Solution().diameterOfBinaryTree(root))
