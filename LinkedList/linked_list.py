class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:

    def __init__(self) -> None:
        self.head = None

    def insertatfirst(self, data):
        new_node = Node(data)
        # when linked list is empty
        if self.head == None:
            self.head = new_node
        else:
            #  when linked list is not empty
            new_node.next = self.head
            self.head = new_node

    def addintheLast(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            current_node = self.head
            while(current_node.next != None):
                current_node = current_node.next
            current_node.next = new_node

    def printlinkedlist(self):
        current_node = self.head
        while(current_node):
            print(current_node.data, end=' ')
            current_node = current_node.next

    def insertAtLocation(self, index, data):
        try:
            #  when linkedList is empty
            if index == 0:
                self.insertatfirst(data)
            #  when linked list is not empty
            else:
                count = 0
                current_node = self.head
                while(count < index-1):
                    current_node = current_node.next
                    count += 1
                
                temp_node = Node(data)
                temp_node.next = current_node.next
                current_node.next = temp_node
        except AttributeError as e:
            print(e)


    def removeLastElement(self):
        # when linked list is empty - do nothing
        if self.head == None:
            print("list is empty")
        #  when linked list has only one element
        elif self.head.next == None:
            self.head = None
            print("Removed the one node now list is empty")
        else:
            #  when linked list has many elements.
            current_node = self.head
            while(current_node.next.next != None):
                current_node = current_node.next
            current_node.next = None

    def addAddAllElements(self, elements):
        #  add elements in the linkedList
        for i in elements:
            self.addintheLast(i)


    def indexOfElement(self, element):
        # if linkedlist in empty
        if self.head == None:
            print("linkedList is empty")

        #  if linkedlist is not emepty
        else:
            current_node = self.head
            count = 0
            while(current_node):
                if current_node.data == element:
                    return (element, count)
                current_node = current_node.next
                count += 1
            return -1
        
    def removeFirstElement(self):
        # When linked List is empty
        if self.head == None:
            return True
        #  When linked list has only one element
        elif self.head.next == None:
            self.head = None
        #  When linked List is not empty
        else:
            current_node = self.head
            self.head = current_node.next
            current_node.next = None

    def lastIndexElement(self, element):
        #  When linkedList is empty
        if self.head == None:
            print("Linked List is not empty")
        else:
            # When linkedList is not empty
            current_node = self.head
            index = 0
            found = -1
            while(current_node):
                if current_node.data == element:
                    found = index
                current_node = current_node.next
                index += 1
            return found
        
    def printcheck(self):
        current_node = self.head
        while(current_node.next.next):
            print(current_node.next)
            current_node = current_node.next

        
    def sizeOfLinkedList(self):
        # if list is empty
        if self.head == None:
            return 0
        else:
            size = 0
            current_node = self.head
            while(current_node):
                size += 1
                current_node = current_node.next
            return size
llist = LinkedList()


# add node to the linked list
# llist.insertatfirst('a')
# llist.insertatfirst('b')
# llist.insertatfirst('c')
# llist.insertatfirst('d')

# llist.printlinkedlist()
# print("============================")
# llist.insertAtLocation(2, 45)
# llist.printlinkedlist()
# print("============================")
# llist.insertAtLocation(0, 5)
# llist.printlinkedlist()
# print("============================")
# llist.insertAtLocation(25, 25)
# llist.printlinkedlist()
# print("============================")
# llist.removeLastElement()
# llist.printlinkedlist()
# print("============================")
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# llist.addAddAllElements(arr)
# llist.printlinkedlist()

llist.addintheLast('a')
llist.printlinkedlist()

# llist.addintheLast('b')
# llist.addintheLast('c')
# llist.printcheck()
# llist.addintheLast('a')
# llist.addintheLast('b')
# llist.addintheLast('a')
# llist.addintheLast('3')
# llist.addintheLast(45)
# llist.addintheLast('b')
# llist.printlinkedlist()
# print("============================")
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# llist.addAddAllElements(arr)
# llist.printlinkedlist()
# a = llist.indexOfElement('b')
# print(a)
# llist.removeFirstElement()
# llist.printlinkedlist()
# print("test")
# llist.removeFirstElement()

# a = llist.lastIndexElement(456)
# print("test")
# print(a)
# a = llist.sizeOfLinkedList()
print("test")
# print(a) 
