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

        1 2 3 4 None
        """
        slow,fast=head,head

        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        
        """
          s
        1 2 3 4 None
        Assign slow.next to second to get  second part of list

                  second
        1 2 -None 3 4 None
        Make sure to end the first half by marking its last node.next as None
        ie to cut both the lists
        If we dont it will go into infinite loop
        """
        second=slow.next
        slow.next = None

        prev=None
        tempHead=second
        # slow.next = None

        while tempHead:
            nextNode = tempHead.next
            tempHead.next=prev
            prev=tempHead
            tempHead = nextNode
        
        h1,h2=head,prev
        while h2:
            h1next=h1.next
            h2next=h2.next

            h1.next=h2
            h2.next=h1next

            h1=h1next  
            h2=h2next       

        return head
        
        

l1 = list_to_linked_list([1, 2, 3, 4, 5, 6])
print_linked_list(l1)
s = Solution()
a = s.reorderList(l1)
print_linked_list(a)
