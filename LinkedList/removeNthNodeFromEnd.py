#  remove Nth node from end of the list
#  i/p = [1, 2, 3, 4, 5]  n = 2
#  o/p = [1, 2, 3, 5]

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
s = Solution()
a = s.removeNthNode(1, l1)
print_linked_list(a)
