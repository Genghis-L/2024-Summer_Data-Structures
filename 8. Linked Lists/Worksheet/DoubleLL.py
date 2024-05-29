#### Original author: Ratan Kumar Dey @ NYU Shanghai ####


class DoubleLinkedList:

    class _Node:
        """Lightweight, nonpublic class for storing a doubly linked node."""

        __slots__ = "_element", "_next", "_prev"  # streamline memory usage

        def __init__(self, element, prev, next):  # initialize node's fields
            self._element = element  # reference to user's element
            self._prev = prev  # reference to prev node
            self._next = next  # reference to next node

    def __init__(self):
        """Create an empty linkedlist."""
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        """Return the number of elements in the list."""
        # TODO
        return self._size

    def is_empty(self):
        """Return True if the list is empty."""
        # TODO
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the list.
        Print if the list is empty.
        """
        # TODO
        if self.is_empty():
            print("The list is empty. ")
            return None
        else:
            return self._head._element

    def last(self):
        """Return (but do not remove) the element at the end of the list.
        Print if the list is empty.
        """
        # TODO
        if self.is_empty():
            print("The list is empty. ")
            return None
        else:
            return self._tail._element

    def delete_first(self):
        """Remove and return the first element of the list.
        Print and return None if the list is empty.
        """
        # TODO
        if self.is_empty():
            print("The list is empty. ")
            return None

        element = self._head._element
        self._head = self._head._next
        if self._head == None:
            # The list is empty
            self._tail = None
            # Set tail to None, and head is already None
        else:
            # The list is not empty
            # Set head.prev to None. If only one element left, then head and tail points to the same Node, head.prev is the same as tail.prev, then tail.prev is automatically set to None.
            # Otherwise, there is no influence on the tail, and we do not need to change head.next.
            self._head._prev = None
        self._size -= 1
        return element

    def delete_last(self):
        """Remove and return the last element of the list.
        Print and return None if the list is empty.
        """
        # TODO
        if self.is_empty():
            print("The list is empty. ")
            return None

        element = self._tail._element
        self._tail = self._tail._prev
        if self._tail == None:
            # The list is empty
            self._head = None
        else:
            # The list is empty
            # Similar as delete_first
            self._tail._next = None
        self._size -= 1
        return element

    def add_first(self, e):
        """Add an element to the front of list."""
        # TODO
        newNode = self._Node(e, None, self._head)
        if self.is_empty():
            # The list is empty
            self._tail = newNode
        else:
            # If the list is not empty, no need to care about tail.
            # Set the previous head.pre to be the inserted one
            self._head._prev = newNode
        self._head = newNode
        self._size += 1

    def add_last(self, e):
        """Add an element to the back of list."""
        # TODO
        newNode = self._Node(e, self._tail, None)
        if self.is_empty():
            # The list is empty
            self._head = newNode
        else:
            # Similar as add_first
            self._tail._next = newNode
        self._tail = newNode
        self._size += 1

    def insert_after_kth_index(self, k, e):
        """Insert an element after the k-th index."""

        if k >= self._size:  # equality as Index starts at 0
            print("The linkedlist is smaller than k.")
            return None

        # Travese to find the k-th place
        curNode = self._head
        for _ in range(k):
            curNode = curNode._next
        # Now the curNode is the place we insert after

        # create the inserted Node
        newNode = self._Node(e, curNode, curNode._next)

        if curNode._next == None:
            # If the inserted place is tail
            self._tail = newNode
        else:
            # If the inserted place is not tail
            curNode._next._prev = newNode

        curNode._next = newNode

        self._size += 1

    def __str__(self):
        result = []
        curNode = self._head
        while curNode is not None:
            result.append(str(curNode._element) + " <--> ")
            curNode = curNode._next
        result.append("None")
        return "".join(result)
