# Calculate maximum height of the tree.
#  Time Complexity - O(n)
#  Auxiliary Space  - O(h)
# Binary Tree Implementation:
'''
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node 
down to the farthest leaf node.

        4
       / \
      2   7
         / \
        6   9
o/p = 3
         
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2
'''

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

if __name__ =='__main__':
    #  create a Node
    root = Node(4)
    root.left = Node(2)
    root.right = Node(7)
    root.right.left = Node(6)
    root.right.right = Node(9)
    print(printheight(root))
