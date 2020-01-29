import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if value is found, return false to indicate no node inserted
        if self.value == value:
            return False
        # value smaller than node, look left
        elif value < self.value:
            # if node exists, continue recursively checking until something is found or inserted
            if self.left:
                return self.left.insert(value)
            # if no node exists, create new one and return true
            else:
                self.left = BinarySearchTree(value)
                return True
        else:
            # if node exists, continue recursively checking until something is found or inserted
            if self.right:
                return self.right.insert(value)
            # if no node exists, create new one and return true
            else:
                self.right = BinarySearchTree(value)
                return True

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # check if target is there, return true if so
        if self.value == target:
            return True
        # if target is less than node value and left node exists, check for value again
        elif target < self.value and self.left:
            return self.left.contains(target)
        # if target is less than node value and right node exists, check for value again
        elif target > self.value and self.right:
            return self.right.contains(target)
        # if target not found, return false
        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        # no right node, return current value
        if self.right == None:
            return self.value
        # if right node, move down and use function again until max is found
        else:
            return self.right.get_max()


    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
