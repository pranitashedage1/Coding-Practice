#  Merge two sorted linked lists - 
#  l1 = [1, 2, 4]
#  l2 = [1, 3, 4]
#  o/p = [1, 1, 2, 3, 4, 4]
# time complexity = O(m + n) > m and n are number of elements in list1 and list2 respectively
#  space complexity = O(1)
# Definition for singly-linked list.
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

#  logic of merging two lists - 
class Solution:
    def mergeTwoLists(self, list1, list2):
        prehead = ListNode(-1)

        prev = prehead
        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            prev = prev.next
        prev.next = list1 if list1 is not None else list2

        return prehead.next

list1 = list_to_linked_list([1, 2, 4])
list2 = list_to_linked_list([1, 3, 4])

s = Solution()
mergedList = s.mergeTwoLists(list1, list2)
print_linked_list(mergedList)
