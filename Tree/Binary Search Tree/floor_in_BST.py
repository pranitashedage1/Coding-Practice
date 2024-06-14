# Floor of the BST - Floor of the BST means finding the greatest smaller value of the given number.
#  Time Complexity - O(h)
#  Auxiliary Space - O(1)
'''
        10
       / \
      5  15
         / \
        12 30

In the above example, when input is 14, then there are 3 smaller values than the 14 which are 10, 5 and 12. But return the greatest values from those 3 smaller values.

When there is no smaller value than the given value then return Null.
Means from above example, i/p is 4 then return Null
if i/p is 30 then return 30
if i/p is 100 then return 30

'''
# Binary Tree Implementation:
class Node:
    def __init__(self, key, left=None, right=None) -> None:
        self.data = key
        self.left = left
        self.right = right

#  Iterative
def find_floor_iterative(node, n):
    if node == None:
        return None
    while(node != None):
        if node.data == n:
            return node
        elif n < node.data:
            node = node.left
        elif n > node.data:
            res = node
            node = node.right

    return res
if __name__ =='__main__':
    #  create a Node
    root = Node(15)
    root.left = Node(5)
    root.right = Node(20)
    root.left.left = Node(3)
    root.right.left = Node(18)
    root.right.right = Node(80)

    a = find_floor_iterative(root, 14)
    print(a.data)
