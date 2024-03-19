'''
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.
Do not modify the linked list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Initialize tortoise and hare pointers
        tortoise = head
        hare = head

        # Move tortoise one step and hare two steps
        while hare and hare.next:
            hare = hare.next.next
            tortoise = tortoise.next

            # check if the hare meets the tortoise
            if tortoise == hare:
                break

        # Check if there is no cycle
        if not hare or not hare.next:
            return None

        # Reset tortoise pointer to head
        tortoise = head

        # Move both pointers by one steps until they meet again
        while tortoise != hare:
            hare = hare.next
            tortoise = tortoise.next
        
        # Return the node where cycle begins
        return tortoise
