# PreOrder Traversal - 
#  Time Complexity - O(n)
#  Auxiliary Space  - O(h)

class Node:
    def __init__(self, key, left=None, right=None) -> None:
        self.data = key
        self.left = left
        self.right = right

def printPreOrder(node):
    if node is None:
        return
    
    print(node.data, end =' ')
    printPreOrder(node.left)
    printPreOrder(node.right)


if __name__ =='__main__':
    #  create a Node
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)

    printPreOrder(root)
