# Calculate maximum height of the tree.
#  Time Complexity - O(n)
#  Auxiliary Space  - O(h)
# Binary Tree Implementation:
'''
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

        4
       / \
      2   7
         / \
        6   9
o/p = 3   as longest path will be [2-4-7-9]
 
Example 1:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:
Input: root = [1,2]
Output: 1
'''
from queue import Queue
class Node:
    def __init__(self, key, left=None, right=None) -> None:
        self.data = key
        self.left = left
        self.right = right

def printheight(root):
    if not root:
        return 0
    left = printheight(root.left)
    right = printheight(root.right)
    height = max(left, right) + 1
    return height

def diameterOfBinaryTree(root, node):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root == None:
        return 0
    left = diameterOfBinaryTree(root.left,node)
    right = diameterOfBinaryTree(root.right, node)
    height = max(left, right) + 1
    if root == node:
        return left + right
    return height

def diameterOfBinaryTreeUsingQueue(root):
    if root == None:
        return None
    q = Queue()
    q.put(root)
    left_count = 0
    while q.empty() == False:
        current_node = q.get()
        if current_node.left:
            q.put(current_node.left)
            

    
    


if __name__ =='__main__':
    #  create a Node
    root = Node(4)
    root.left = Node(2)
    root.right = Node(7)
    root.right.left = Node(6)
    root.right.right = Node(9)
    # print(printheight(root))
    print(diameterOfBinaryTree(root, root))

