# Binary Tree Implementation:

'''4 becomes left child of 2
        1
       / \
      2   3
     / \ / \
    4 None None None
   / \
   None None'''

class Node:
    def __init__(self, key, left=None, right=None) -> None:
        self.val = key
        self.left = left
        self.right = right

if __name__ =='__main__':
    #  create a Node
    root = Node(1)
    root.left = Node(2)
    ''' 2 and 3 become left and right children of 1
       1
      /  \
     2    3
    / \  / \
   None None None None'''

    root.right = Node(3)
    root.left.left = Node(4)

