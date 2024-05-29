#### Original author: Ratan Kumar Dey @ NYU Shanghai ####


class SingleLinkedList:

    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""

        __slots__ = "_element", "_next"  # streamline memory usage

        def __init__(self, element, next):  # initialize node's fields
            self._element = element  # reference to user's element
            self._next = next  # reference to next node

    def __init__(self):
        """Create an empty linkedlist."""
        self._head = None
        self._size = 0

    def __len__(self):
        """Return the number of elements in the linkedlist."""
        # TODO
        return self._size

    def is_empty(self):
        """Return True if the linkedlist is empty."""
        # TODO
        return self._size == 0

    def top(self):
        """Return (but do not remove) the element at the top of the linkedlist.
        Print if the linkedlist is empty and return None.
        """
        # TODO
        if self.is_empty():
            print("The linkedlist is empty. ")
            return None
        else:
            return self._head._element

    def insert_from_head(self, e):
        """Add element e to the head of the linkedlist."""
        # TODO
        new_node = self._Node(e, self._head)  # Create a new Node
        self._head = new_node  # Set the new Node as the head
        self._size += 1

    def delete_from_head(self):
        """Remove and return the element from the head of the linkedlist.
        Print if the linkedlist is empty and return None.
        """
        # TODO
        if self.is_empty():
            print("The linkedlist is empty. ")
            return None
        else:
            element = self._head._element  # element is the removed head element
            self._head = self._head._next  # Change the head to the successor
            self._size -= 1
            return element

    def __str__(self):
        result = []
        curNode = self._head
        while curNode is not None:
            result.append(str(curNode._element) + "-->")
            curNode = curNode._next
        result.append("None")
        return "".join(result)

    def return_max(self):
        """Find and return the largest element in the linkedlist.
        Print if the linkedlist is empty and return None.
        """
        # TODO
        if self.is_empty():
            print("The linkedlist is empty. ")
            return None
        else:
            max_element = self._head._element
            curNode = self._head._next  # Interator, No need to check the first head
            # Trverse to find the max_element
            while curNode is not None:
                if curNode._element > max_element:
                    max_element = curNode._element
                curNode = curNode._next
            return max_element

    def insert_after_kth_index(self, k, e):
        """Insert an element after the kth index in the list, the index starts at 0.
        Print if the linkedlist is smaller than k.
        """
        # TODO
        if k >= self._size:  # equality as Index starts at 0
            print("The linkedlist is smaller than k.")
            return None
        else:
            curNode = self._head
            # Traverse the linkedlist k steps, so that curNode is the place where we insert after
            for _ in range(k):
                curNode = curNode._next

            new_Node = self._Node(e, curNode._next)
            # create a new Node with ref to the successor of curNode
            curNode._next = new_Node  # change the ref of the curNode to the new Node
            self._size += 1
