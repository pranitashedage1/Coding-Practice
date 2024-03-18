'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.
Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]
'''
#  remove Nth node from end of the list
#  i/p = [1, 2, 3, 4, 5]  n = 2
#  o/p = [1, 2, 3, 5]
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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        start, end = dummy, dummy
        dummy.next = head
        # Advances first pointer so that the gap between first and second is n nodes apart
        for i in range(n+1):
            end = end.next
        # Move first to the end, maintaining the gap
        while end:
            end = end.next
            start = start.next
        start.next = start.next.next
        return dummy.next

    def removeNthNode(self, nodeIndex, ll):
        length = self.calculateLength(ll)
        if length == nodeIndex:
            return ll.next
        remove = length - nodeIndex
        count = 0
        current_node = ll
        while(count < remove-1):
            current_node = current_node.next
            count += 1 
        
        current_node.next = current_node.next.next
        return ll

    def calculateLength(self, ll):
        current_node = ll
        count = 0
        while(current_node):
            count += 1
            current_node = current_node.next
        
        return count

l1 = list_to_linked_list([1, 2])
l2 = list_to_linked_list([3, 4, 5, 7, 8, 80])
s = Solution()
a = s.removeNthNode(1, l1)
print_linked_list(a)
b = s.removeNthFromEnd(l2, 2)
print_linked_list(b)
