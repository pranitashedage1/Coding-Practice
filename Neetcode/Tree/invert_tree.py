# Invert Tree Methods.
# Binary Tree Implementation:
'''
        4
       / \
      2   7
     / \ / \
    1  3 6  9

        4
       / \
      7   2
     / \ / \
    9  6 3  1

Given the root of a binary tree, invert the tree, and return its root.

Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: []
'''
from queue import Queue
from collections import deque
import collections
class Node:
    def __init__(self, key, left=None, right=None) -> None:
        self.data = key
        self.left = left
        self.right = right


def printNodesByLevels(node):
    if node == None:
        return
    q = Queue()
    q.put(node)
    while q.empty() == False:
        current = q.get()
        print(current.data, end=' ')
        if current.left != None:
            q.put(current.left)
        if current.right != None:
            q.put(current.right)
'''
        4
       / \
      2   7
     / \ / \
    1  3 6  9

'''
def invertTreeOtherApproach(root):
    if not root:
        return None
    root.right, root.left = root.left, root.right
    invertTreeOtherApproach(root.right)
    invertTreeOtherApproach(root.left)
    return root

def invertTree(root):
    if not root:
            return None
    right = invertTree(root.right)
    left = invertTree(root.left)
    root.left = right
    root.right = left
    return root

def invertNodeUsingQueue(root):
    queue = collections.deque([root])
    while queue:
        current_element = queue.popleft()
        current_element.left, current_element.right = current_element.right, current_element.left
        if current_element.left:
            queue.append(current_element.left)
        
        if current_element.right:
            queue.append(current_element.right)

    return root

if __name__ =='__main__':
    #  create a Node
    root = Node(4)
    root.left = Node(2)
    root.right = Node(7)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(6)
    root.right.right = Node(9)

    printNodesByLevels(root)
    # invertTree(root)
    # invertTreeOtherApproach(root)
    invertNodeUsingQueue(root)
    print()
    printNodesByLevels(root)
