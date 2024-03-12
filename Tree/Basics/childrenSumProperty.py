# Sum of children - 
# Time complexity - O(n)
# Auxiliary space - O(h)

'''
  children sum property means - sum of left child and right child is equal to the root.

Example 1) - 

        20
       / \
      8  12
     / \ / \
    3  5 N  
  
    o/p = Yes

Example 2) - 

        10
       / \
      8   2
         / \
        2  

    o/p = Yes

Example 3) - 

        3
       / \
      1   2
         / \
        1   2

    o/p = No

   '''
from queue import Queue

class Node:
    def __init__(self, key, left=None, right=None) -> None:
        self.data = key
        self.left = left
        self.right = right

def children_sum(node):
    if node == None:
        return True
    if node.left == None and node.right == None:
        return True
    sum = 0
    if node.left != None:
        sum += node.left.data
    if node.right != None:
        sum += node.right.data
    return node.data == sum and children_sum(node.left) and children_sum(node.right)


if __name__ =='__main__':
    #  create a Node
    root = Node(10)
    root.left = Node(8)
    root.right = Node(2)
    root.right.left = Node(2)
    a = children_sum(root)
    print(a)
