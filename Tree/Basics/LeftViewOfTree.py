# Left View of the tree
#  Time Complexity - O(n)
#  Auxiliary Space  - O(h)
# Binary Tree Implementation:
'''
        1
       / \
      N   3
         / \
        6   N
       / \
      16  8
here o/p will be - 1, 3, 6, 16  - From every level only left most element will get print
'''

'''4 becomes left child of 2
        1
       / \
      2   3
     / \ / \
    4  5 N  6
   / \
   N  N'''
from queue import Queue
class Node:
    def __init__(self, key, left=None, right=None) -> None:
        self.data = key
        self.left = left
        self.right = right
class Test:
    #  create a maxLevel variable that will be shared amoong the all calls.
    #  Debug a code step by step to understand.
    def __init__(self) -> None:
        self.maxLevel = 0

    def leftViewOfTree(self, node, level):
        if node == None:
            return
        if self.maxLevel < level:
            print(node.data, end=" ")
            self.maxLevel = level
        self.leftViewOfTree(node.left, level+1)
        self.leftViewOfTree(node.right, level+1)

    def printNodesByLevelsTwoLoops(self, node):
        if node == None:
            return
        q = Queue()
        q.put(node)
        while q.empty() == False:
            count = q.qsize()
            for i in range(count):
                current = q.get()
                if i == 0:
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
    root.right.left = Node(40)
    root.left.left = Node(4)
    root.left.right = Node(5)
    # root.right.left.right = Node(6)
    # root.right.right.right = Node(8)
    maxLevel = 0
    t = Test()
    # t.leftViewOfTree(root, 1)
    t.printNodesByLevelsTwoLoops(root)

# Size of the tree can also be done by using queue instead of recursion.
# Time complexity will be same as of above solution.
# Auxiliary space will vary as per width of the queue.
