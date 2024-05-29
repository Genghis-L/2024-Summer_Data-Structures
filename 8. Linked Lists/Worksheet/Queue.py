from DoubleLL import DoubleLinkedList

class Queue:

    def __init__(self):
        """Create an empty queue consisting of an empty double linkedlist."""
        self._inside = DoubleLinkedList()

    def __len__(self):
        """Return the number of elements in the queue."""
        return len(self._inside)

    def is_empty(self):
        """Return True if the queue is empty."""
        pass
    
    def peek(self):
        """Return (but do not remove) the element at the head of the queue.
           Return None if the queue is empty.
        """
        pass

    def enqueue(self, e):
        """Add element e to the tail of the queue."""
        pass

    def dequeue(self):
        """Remove and return the element from the head of the queue.
           Return None if the queue is empty.
        """
        pass

    def __str__(self):
        return str(self._inside)

