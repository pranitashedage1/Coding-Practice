# Reverse the linked list -
# i/p = [1, 2, 3, 4, 5]
#  o/p = [5, 4, 3, 2, 1]
# time complexicity - O(n)
# space complexicity - O(1)
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

def print_linked_list(head):
    current_node = head
    while current_node:
        print(current_node.val, end=" ")
        current_node = current_node.next
    print()  # Print a newline at the end

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#  logic of reverse the linked list
class Solution:
    def reverseList(self, head):
        prev = None
        current_node = head

        while current_node:
            temp_node = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = temp_node        
        return prev

my_list = [1, 2, 3, 4, 5]
my_linked_list = list_to_linked_list(my_list)

s = Solution()
a = s.reverseList(my_linked_list)
print_linked_list(a)
