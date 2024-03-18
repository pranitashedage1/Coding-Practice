# Sum of the elements of the linked list. Each nodes has only single digit, if sum goes above 10 then 
#  shift carry on to the next digit.
# Input: l1 = [2,4,3], l2 = [5,6,4]    
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Input: l1 = [0], l2 = [0]   
# Output: [0]

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

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
    def addTwoNumbers(self, l1, l2):
        list1 = l1
        list2 = l2
        d = 0
        new_node = ListNode(-1)
        test = new_node
        while list1 or list2 or d:
            a = list1.val if list1 else 0
            b = list2.val if list2 else 0
            c = (a + b + d) % 10
            d = (a + b + d) // 10
            new = ListNode(c)
            test.next = new
            test = test.next
            if list1:
                list1 = list1.next
            if list2:
                list2 = list2.next
        return new_node.next

l1 = list_to_linked_list([2, 4, 3])
l2 = list_to_linked_list([5, 6, 4])
s = Solution()
a = s.addTwoNumbers(l1, l2)
print_linked_list(a)
