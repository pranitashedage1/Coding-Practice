#  Reorder List - 
#  i/p = [1, 2, 3, 4, 5, 6]
#  o/p = [1, 6, 2, 5, 3, 4]
#  for this - 
#  i) Find the middle of the list and sparatate the two lists
#  ii) Reorder the second list.
#  iii) merge te first list and reordered list.

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
    def reorderList(self, head) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # Find the middle point of the linked List

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # reverse the second list
        prev = None
        current_node = slow
        while(current_node):
            temp_node = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = temp_node

            # alternatively
            # current_node.next, prev, current_node = prev, current_node, current_node.next
        
        # return head, prev

        # merge the two lists 
        #  1, 2, 3
        #  5, 4, 3
        first = head
        second = prev

        while(second.next):
            temp = first.next
            first.next = second
            first = temp

            temp = second.next
            second.next = first
            second = temp

            #  we can write below code alternatively
            # first.next, first = second, first.next
            # second.next, second= first, second.next

        return head

l1 = list_to_linked_list([1, 2, 3, 4, 5, 6])
print_linked_list(l1)
s = Solution()
a = s.reorderList(l1)
print_linked_list(a)
