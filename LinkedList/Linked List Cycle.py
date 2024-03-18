# Linked List Cycle - 
# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by 
# continuously following the next pointer.
# Internally, pos is used to denote the index of the node that tail's next pointer is connected to.
#  Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Input: head = [1,2], pos = 0
# Output: true
# Input: head = [1], pos = -1
# Output: false
from typing import Optional
def print_linked_list(head):
    current_node = head
    while current_node:
        print(current_node.val, end=" ")
        current_node = current_node.next
    print()  # Print a newline at the end

def list_to_linked_list(input_list):
    if not input_list:
        return None  # Return None for an empty list

    # Create the first node
    head = ListNode(input_list[0])
    current_node = head

    # Iterate through the remaining elements in the list
    for value in input_list[1:]:
        current_node.next = ListNode(value)
        current_node = current_node.next
    return head

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle1(self, head) -> bool:
        set1 = set()
        while head:
            if head not in set1:
                set1.add(head)
            else:
                return True
            head = head.next
        return False

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow, fast = head, head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True

s = Solution()
l1 = list_to_linked_list([1, 3, 6])
a = s.hasCycle1(l1)
b = s.hasCycle(l1)
print(a)
print(b)
#  This will only give false as - list_to_linked_list function always gives linked list with 
#  the last node having next pointer pointint to the null. But this code will work for the 
#  linked lists having cycle in it.
