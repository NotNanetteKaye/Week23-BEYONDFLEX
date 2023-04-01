from node import Node

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None # ending point
        pass

    def append_node(self, data): # responsible for adding nodes to the end of the list
        node = Node(data)

        if self.head is None:
            self.head = Node # this node becomes the starting point
            self.tail = Node # in the beginning, the head and tail node are the same, & will
            # eventually differ if the linked list as >1 node objects
            return # return once linked list head is defined
        else:
            self.tail.next = node
            self.tail = self.tail.next