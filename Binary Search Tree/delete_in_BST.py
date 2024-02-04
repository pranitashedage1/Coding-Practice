# Delete the node in BST
#  Time Complexity - O(h)
#  Auxiliary Space -  O(h) Since it is a recursive function
# Binary Tree Implementation:
class Node:
    def __init__(self, key, left=None, right=None) -> None:
        self.data = key
        self.left = left
        self.right = right
# Recursion
def get_successor(node):
    current = node.right
    if current != None and current.left != None:
        current = current.left
    return current

def delete_form_BST(node, n):
    if node == None:
        return None
    if n < node.data:
        node.left = delete_form_BST(node.left, n)
    elif n > node.data:
        node.right = delete_form_BST(node.right, n)
    else:
        if node.left == None:
            return node.right
        elif node.right == None:
            return node.left
        else:
            successor = get_successor(node)
            node.data = successor.data
            node.right = delete_form_BST(node.right, successor.data)
    return node

if __name__ =='__main__':
    #  create a Node
    root = Node(15)
    root.left = Node(5)
    root.right = Node(20)
    root.left.left = Node(3)
    root.right.left = Node(18)
    root.right.right = Node(80)

    a = delete_form_BST(root, 15)
    print(a)
