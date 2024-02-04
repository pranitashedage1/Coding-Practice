class Node:
    def __init__(self, data=None, prev=None, next=None) -> None:
        self.data = data
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def appendDll(self, element):
        # It will append element in the last
        new_Node = Node(element)
        if not self.head:
            self.head = new_Node
        
        else:
            current_node = self.head
            while(current_node.next != None):
                current_node = current_node.next
            current_node.next = new_Node
            new_Node.prev = current_node
    
    def popLastElementDll(self):
        # Remove element form the last
        if not self.head:
            print("doubly linked list is empty")
        elif self.head.next == None:
            self.head = None
        else:
            current_node = self.head
            while(current_node.next.next):
                current_node = current_node.next
            
            current_node.next = None

    def printDll(self):
        current_node = self.head
        while(current_node):
            print(current_node.data)
            current_node = current_node.next

    def insertAfterElement(self, before_element, element):
        new_node = Node(element)

        current_node = self.head
        found = 0
        while(current_node):
            if current_node.data == before_element:
                found = 1
                break
            current_node = current_node.next
        if found:
            if self.head.next != None:
                new_node.next = current_node.next
                new_node.prev = current_node
                
                current_node.next.prev = new_node
                current_node.next = new_node
            else:
                #  when doubly linked list has only one element
                self.head.next = new_node
                new_node.prev = self.head
                print("worked")

        else:
            print("element not found")

    def insertBeforeElement(self, after_element, element):
        new_node = Node(element)
        current_node = self.head
        found = 0
        if self.head.next != None:
            #  doubly linked list has more than one element
            while(current_node):
                if current_node.data == after_element:
                    found = 1
                    break
                current_node = current_node.next
            if found:
                new_node.next = current_node
                new_node.prev = current_node.prev
                current_node.prev.next = new_node 
                current_node.prev = new_node
            else:
                print("Element not found")
        else:
            #  doubly linked list has one element
            self.head.next = new_node
            new_node.prev = self.head

dll = DoublyLinkedList()
dll.appendDll(1)
dll.appendDll(2)
dll.appendDll(5)
dll.printDll()
print("==============")
# dll.popLastElementDll()
dll.insertAfterElement(2, 3)
dll.printDll()
print("==============")
# dll.insertAfterElement(1, 2)
dll.insertBeforeElement(5, 4)
dll.printDll()
print("==============")
