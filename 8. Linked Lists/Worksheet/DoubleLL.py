#### Original author: Ratan Kumar Dey @ NYU Shanghai ####

class DoubleLinkedList:

    class _Node:
        """Lightweight, nonpublic class for storing a doubly linked node."""
        __slots__ = '_element', '_next', '_prev'         # streamline memory usage

        def __init__(self, element, prev, next):      # initialize node's fields
            self._element = element               # reference to user's element
            self._prev = prev                     # reference to prev node
            self._next = next                     # reference to next node




    def __init__(self):
        """Create an empty linkedlist."""
        self._head = None
        self._tail = None
        self._size = 0


    def __len__(self):
        """Return the number of elements in the list."""
        #TODO
        pass

    def is_empty(self):
        """Return True if the list is empty."""
        #TODO
        pass

    def first(self):
        """Return (but do not remove) the element at the front of the list.
           Print if the list is empty.
        """
        #TODO
        pass

    def last(self):
        """Return (but do not remove) the element at the end of the list.
           Print if the list is empty.
        """
        #TODO
        pass


    def delete_first(self):
        """Remove and return the first element of the list.
           Print and return None if the list is empty.
        """
        #TODO
        pass

    def delete_last(self):
        """Remove and return the last element of the list.
           Print and return None if the list is empty.
        """
        #TODO
        pass


    def add_first(self, e):
        """Add an element to the front of list."""
        #TODO
        pass


    def add_last(self, e):
        """Add an element to the back of list."""
        #TODO
        pass


    def __str__(self):
        result = []
        curNode = self._head
        while (curNode is not None):
            result.append(str(curNode._element) + " <--> ")
            curNode = curNode._next
        result.append("None")
        return "".join(result)
