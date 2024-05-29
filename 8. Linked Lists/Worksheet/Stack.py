from SingleLL import SingleLinkedList

class Stack:

    def __init__(self):
        """Create an empty stack consisting of an empty linkedlist."""
        self._inside = SingleLinkedList()

    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self._inside)

    def is_empty(self):
        """Return True if the stack is empty."""
        pass
    
    def peek(self):
        """Return (but do not remove) the element at the top of the stack.
           Return None if the stack is empty.
        """
        pass

    def push(self, e):
        """Add element e to the top of the stack."""
        pass

    def pop(self):
        """Remove and return the element from the top of the stack.
           Return None if the stack is empty.
        """
        pass

    def __str__(self):
        return str(self._inside)

