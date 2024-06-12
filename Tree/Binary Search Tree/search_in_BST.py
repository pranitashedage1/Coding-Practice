# Search the node in BST
# Time Complexity - O(h)
# Auxiliary Space by Recursion - O(h)
# Auxiliary space by iteration - O(1)
# Binary Tree Implementation:
class Node:
    def __init__(self, key, left=None, right=None) -> None:
        self.data = key
        self.left = left
        self.right = right
# Recursion
def search_in_binary_search_tree(node, n):
    if node == None:
        return False
    if node.data == n:
        return True
    if n < node.data:
        return search_in_binary_search_tree(node.left, n)
    else:
        return search_in_binary_search_tree(node.right, n)
# Iterative Solution
def search_in_binary_search_tree_iterative(node, n):
    while(node != None):
        if node.data == n:
            return True
        if n < node.data:
            node = node.left
        else:
            node = node.right
    return False

if __name__ =='__main__':
    #  create a Node
    root = Node(15)
    root.left = Node(5)
    root.right = Node(20)
    root.left.left = Node(3)
    root.right.left = Node(18)
    root.right.right = Node(80)

    print(search_in_binary_search_tree(root, 19))
    print(search_in_binary_search_tree_iterative(root, 3))
