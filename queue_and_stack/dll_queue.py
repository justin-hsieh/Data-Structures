import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.dll = DoublyLinkedList()

    def enqueue(self, value):
        self.dll.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if (self.size == 0):
            pass
        else:
            value = self.dll.remove_from_head()
            self.size -= 1
            return value

    def len(self):
        return self.size
