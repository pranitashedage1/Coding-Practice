# Print all nodes at Kth height
#  Time Complexity - O(n)
#  Auxiliary Space  - O(h)
'''4 becomes left child of 2
        1
       / \
      2  3
     / \ / \
    4  5 N  6
   / \     /  \ 
   N  N   N   80 '''

class Node:
    def __init__(self, key, left=None, right=None) -> None:
        self.data = key
        self.left = left
        self.right = right


def printNodesAtKthDistace(node, k):
    if node == None:
        return
    if k == 0:
        print(node.data, end=' ')
    else:
        printNodesAtKthDistace(node.left, k-1)
        printNodesAtKthDistace(node.right, k-1)

if __name__ =='__main__':
    #  create a Node
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)

    printNodesAtKthDistace(root, 2)
