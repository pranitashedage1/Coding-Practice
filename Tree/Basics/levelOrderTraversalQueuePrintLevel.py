# Print the nodes by level 
# Time complexity - O(n)
# Auxiliary space - 0(w) where w will be the width of the binary tree.

#  we run a loop while the queue is not empty.
#  We will enqueue a root in the queue
#  then we will dequeue it and print it.
#  after deque, it will enqueue children of the root
# We will continue this process untill queue gets empty.
'''4 becomes left child of 2
        1
       / \
      2  3
     / \ / \
    4  5 N  6
   / \     /  \ 
   N  N   N   8
   
   o/p - [1, 2, 3, 4, 5, 6, 8] print node by line and by level
   After every level print next nodes on the new line
   1 
   2 3 
   4 5 6
   '''
from queue import Queue
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

def printNodesByLevels(node):
    if node == None:
        return
    q = Queue()
    q.put(node)
    q.put(None)
    while q.qsize()>1:
        current = q.get()
        if current == None:
            q.put(None)
            print()
        else:
            print(current.data, end=" ")
            if current.left != None:
                q.put(current.left)
            if current.right != None:
                q.put(current.right)

def printNodesByLevelsTwoLoops(node):
    if node == None:
        return
    q = Queue()
    q.put(node)
    while q.empty() == False:
        count = q.qsize()
        for i in range(count):
            current = q.get()
            print(current.data, end =' ')
            if current.left != None:
                q.put(current.left)
            if current.right != None:
                q.put(current.right)
        print()

if __name__ =='__main__':
    #  create a Node
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)

    # printNodesByLevels(root)

#  Another approach for above method 
    printNodesByLevelsTwoLoops(root)
