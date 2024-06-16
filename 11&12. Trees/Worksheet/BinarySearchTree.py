from BSTNode import BSTNode


class BinarySearchTree:

    def __init__(self):
        self._root = None

    def is_empty(self):
        """Returns True if this tree is empty, False otherwise"""
        return self._root == None

    def get_root(self):
        """Returns the node at the root of this tree, None if it's empty"""
        return self._root

    def height(self):
        """Returns the height of the tree, 0 if it's empty"""
        # TODO
        if self.is_empty():
            return 0
        return self._root.height()

    def add(self, v):
        """
        Inserts value v in this tree
        Returns a reference to the node that contains v
        """
        # TODO
        if self.is_empty():
            self._root = BSTNode(v)
            n = self._root
        else:
            n = self._root.add(v)
        return n

    def find(self, v):
        """
        Returns a reference to the node that contains v
        None if the tree doesn't contain v
        """
        # TODO
        if self.is_empty():
            return None
        else:
            return self._root.find(v)

    def list_in_order(self):
        """
        Returns the sorted list of all values in this tree
        *** [] if it's empty ***
        *** Duplicates included ***
        """
        # TODO
        if self.is_empty():
            return []
        else:
            return self._root.list_in_order()

    def list_breadth_first(self):
        """
        Returns the level-ordered list of all values in this tree
        *** [] if it's empty ***
        *** Duplicates included ***
        """
        # TODO
        if self.is_empty():
            return []

        # Initialize the level-ordered list and a queue
        result = []
        queue = [self._root]

        while queue:
            # dequeue and store the first elmt
            curNode = queue.pop(0)
            result.extend([curNode.value] * curNode.counter)
            # first append left, second append right
            if curNode._left is not None:
                queue.append(curNode._left)
            if curNode._right is not None:
                queue.append(curNode._right)
            # all the elmts in the same layer has been appended from left to right, layer by layer

        return result

    def remove(self, v):
        """
        Removes value v from the tree
        #Skip node removal if
        #       (a) value doesn't occur in the tree
        #       (b) counter is higher than 1 (decrement counter)
        Returns a reference to the node containing v (we did not use this return)
        """
        # TODO
        n = self.find(v)
        # Case (a): value doesn't occur in the tree
        if not n:
            return None
        # Case (b): counter is higher than 1 (decrement counter)
        if n.counter > 1:
            n.counter -= 1
        # Case (c): the removed node is the root
        elif n == self._root:
            self._root = n.remove()
            if self._root is not None:
                # The case that the removed node has one child, reset the parent
                self._root._parent = None
        # Regular case
        else:
            n.remove()
        return n
