'''
Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.

You can think of the left and right pointers as synonymous to the predecessor and 
successor pointers in a doubly-linked list. For a circular doubly linked list, 
the predecessor of the first element is the last element, and the successor of the last element
 is the first element.

We want to do the transformation in place. After the transformation, 
the left pointer of the tree node should point to its predecessor, and 
the right pointer should point to its successor. 
You should return the pointer to the smallest element of the linked list.
Example 1:
Input: root = [4,2,5,1,3]
Output: [1,2,3,4,5]
Explanation: The figure below shows the transformed BST. The solid line indicates the successor
 relationship, while the dashed line means the predecessor relationship.

Example 2:
Input: root = [2,1,3]
Output: [1,2,3]
'''
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
                if curr.left is None:
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

