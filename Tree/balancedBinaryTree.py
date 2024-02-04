# Balance Binary Tree:
# Time complexity - 
# Auxiliary space - 

'''
  Height of left sub tree and right sub tree should not be greater than 1.

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

   '''
from queue import Queue

class Node:
    def __init__(self, key, left=None, right=None) -> None:
        self.data = key
        self.left = left
        self.right = right

def balanced_bianry_tree(node):
    if node == None:
        return 0
    left = balanced_bianry_tree(node.left)
    if (left == -1):
        return -1
    right = balanced_bianry_tree(node.right)
    if right == -1:
        return -1
    if abs(left-right) > 1:
        return -1
    else:
        return max(left, right) + 1

if __name__ =='__main__':
    #  create a Node
    root = Node(10)
    root.left = Node(8)
    root.right = Node(2)
    root.right.left = Node(2)
    # root.right.left.right = Node(2)
    a = balanced_bianry_tree(root)
    print(a)
