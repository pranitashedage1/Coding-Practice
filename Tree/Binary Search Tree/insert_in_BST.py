# Insert the node in BST
#  Time Complexity for both recursion and iterative - O(h)
#  Auxiliary Space by Recursion - O(h)
#  Auxiliary space by iteration - O(1)
# Binary Tree Implementation:

class Node:
    def __init__(self, key, left=None, right=None) -> None:
        self.data = key
        self.left = left
        self.right = right

    
# Recursion
def insert_in_binary_search_tree(node, n):
    if node == None:
        return Node(n)
    if n < node.data:
        node.left =  insert_in_binary_search_tree(node.left, n)
    elif n > node.data:
        node.right = insert_in_binary_search_tree(node.right, n)
    return node

# Iterative Solution
def insert_in_binary_search_tree_iterative(node, n):
    temp = Node(n)
    parent = None
    current = node
    while(current != None):
        parent = current
        if n < current.data:
            current = current.left
        elif n > current.data:
            current = current.right
        else:
            return node
    if parent == None:
        return temp
    if n > parent.data:
        parent.right = temp
    else:
        parent.left = temp
    return node

if __name__ =='__main__':
    #  create a Node
    root = Node(15)
    root.left = Node(5)
    root.right = Node(20)
    root.left.left = Node(3)
    root.right.left = Node(18)
    root.right.right = Node(80)

    a = insert_in_binary_search_tree(root, 19)
    print(a)
    b = insert_in_binary_search_tree_iterative(root, 3)
    print(b)
    c = insert_in_binary_search_tree_iterative(root, 5)
    print(c)

def inorderTraversal(node):
    if not node:
        return None
    inorderTraversal(node.left)
    print(node.data, end=" ")
    inorderTraversal(node.right)

inorderTraversal(root)
