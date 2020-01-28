import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.dll = DoublyLinkedList()

    def push(self, value):
        self.dll.add_to_head(value)
        self.size += 1

    def pop(self):
        if (self.size == 0):
            pass
        else:
            value = self.dll.remove_from_head()
            self.size -= 1
            return value

    def len(self):
        return self.size
