# Print the nodes by level 
# Time complexity - 
#  i) To find height - O(n)
#  ii) To prints the nodes from all levels O(h*n)

'''4 becomes left child of 2
        1
       / \
      2  3
     / \ / \
    4  5 N  6
   / \     /  \ 
   N  N   N   8
   
   o/p - [1, 2, 3, 4, 5, 6, 8] print node by line and by level
   '''

class Node:
    def __init__(self, key, left=None, right=None) -> None:
        self.data = key
        self.left = left
        self.right = right

def printheight(node):
    if node == None:
        return 0
    left = printheight(node.left)
    right = printheight(node.right)
    maximum = max(left, right) + 1
    return maximum

def printNodesByLevels(node, k):
    if node == None:
        return
    if k == 0:
        print(node.data, end=' ')
    else:
        printNodesByLevels(node.left, k-1)
        printNodesByLevels(node.right, k-1)

if __name__ =='__main__':
    #  create a Node
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)

    height = printheight(root)
    for i in range(height):
        printNodesByLevels(root, i)
