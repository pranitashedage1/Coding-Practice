# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head
        current_node = head
        while current_node:
            new_node = Node(current_node.val)
            new_node.next = current_node.next
            current_node.next = new_node
            current_node = new_node.next
            # if new_node.next == None:
            #     current_node = current_node.next.next
            # else:
            #     current_node = None    
        current_node = head
        while current_node:
            if current_node.random != None:
                current_node.next.random = current_node.random.next if current_node.random else None
            current_node = current_node.next.next    
        old_list = head
        new_list = head.next
        head_new = head.next
        while old_list:
            old_list.next = old_list.next.next
            new_list.next = new_list.next.next if new_list.next else None
            old_list = old_list.next
            new_list = new_list.next
        return head_new
