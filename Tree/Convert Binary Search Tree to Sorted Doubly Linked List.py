class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if root:
            head = Node()  # fake node for a start
            prev = head     # remember previous node
            curr = root     # start from the root
            while curr:
                # this is the most left unprocessed node
                if not curr.left:
                    curr.left = prev
                    # if we don't assign prev right to curr then
                    # head.right.left = prev will throw exception
                    # since head.right will not be assigned to curr
                    prev.right = curr
                    prev = curr
                    curr = curr.right
                else:
                    rightmost = curr.left  # find the rightmost child
                    while rightmost.right:
                        rightmost = rightmost.right
                    if not rightmost.right:  # found the rightmost
                        rightmost.right = curr
                        temp = curr           # remember curr to invalidate its left pointer
                        curr = curr.left
                        temp.left = None     # we can also set it right away temp.left = rightmost but then we need to check for it
            prev.right = head.right     # at the end prev point to the last node
            head.right.left = prev      # replace fake node with the last node in the tree
            head = head.right
            return head
        return None


if __name__ =='__main__':
    #  create a Node
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(3)
    print(Solution().treeToDoublyList(root))