'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.
Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []
'''
from typing import Optional, List

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
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        while len(lists) > 1:
            mergedList = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i+1) < len(lists) else None
                mergedList.append(self.mergeTwoLists(l1, l2))
            lists = mergedList
        return lists[0]

    def mergeTwoLists(self, l1, l2):
        # todo
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next

list1 = list_to_linked_list([1, 2, 7])
list2 = list_to_linked_list([1, 3, 4])
list3 = list_to_linked_list([6, 7, 8])
list4 = list_to_linked_list([8, 10, 12])
list5 = list_to_linked_list([10, 14])

s = Solution()
mergedList = s.mergeKLists([list1, list2, list3, list4, list5])
print_linked_list(mergedList)
# Output : 1 1 2 3 4 6 7 7 8 8 10 10 12 14 
