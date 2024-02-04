# Size of Binary Tree using recursion
# Size of Binary Tree means number of nodes
#  Time Complexity - O(n)
#  Auxiliary Space  - O(h)
# Binary Tree Implementation:
'''4 becomes left child of 2
        1
       / \
      2   3
     / \ / \
    4  5 N  6
   / \
   N  N'''

class Node:
    def __init__(self, key, left=None, right=None) -> None:
        self.data = key
        self.left = left
        self.right = right

def sizeOfBinaryTree(node):
    if node == None:
        return 0
    return 1 + sizeOfBinaryTree(node.left) + sizeOfBinaryTree(node.right)

if __name__ =='__main__':
    #  create a Node
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)
    print(sizeOfBinaryTree(root))

# Size of the tree can also be done by using queue instead of recursion. 
# Time complexity will be same as of above solution.
# Auxilary space will vary as per width of the queue.
