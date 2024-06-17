class BSTNode:
    # The definition of subtree of a node in this context includes the node itself
    def __init__(self, new_value):
        self.value = new_value
        self.counter = 1
        self._left = None
        self._right = None
        self._parent = None

    def is_leaf(self):
        """Returns True if this node is a leaf, False otherwise"""
        # TODO
        return (self._left is None) and (self._right is None)

    def nb_of_children(self):
        """
        Returns the number of children this node has
        0 => node is a leaf
        1 => node has a unique child (right or left)
        2 => node has two children (right and left)
        """
        # TODO
        result = 0
        if self._left is not None:
            result += 1
        if self._right is not None:
            result += 1
        return result

    def height(self):
        """Returns the height of the subtree of this node (min. is 1)"""
        # TODO
        height = 1
        # If self is not a leaf
        if not self.is_leaf():
            if self._left is not None:
                height = 1 + self._left.height()
            if self._right is not None:
                height = max(height, 1 + self._right.height())
        # If self is a leaf
        return height

    def add(self, v):
        """
        Inserts value v in this node's subtree
        If v is already present, increment the counter on the container node
        Otherwise, add a new node containing value v
        Returns a reference to the newly added node
        """
        # TODO
        # Case of duplicates, add the counter
        if v == self.value:
            self.counter += 1
            return self

        # Case of No duplicates
        # Add on the left side
        if v < self.value:
            # If the position is empty
            if self._left is None:
                added_node = BSTNode(v)
                self._left = added_node
                self._left._parent = self
            else:
                added_node = self._left.add(v)
        # Add on the right side
        else:
            # If the position is empty
            if self._right is None:
                added_node = BSTNode(v)
                self._right = added_node
                self._right._parent = self
            else:
                added_node = self._right.add(v)
        return added_node

    def find(self, v):
        """
        Returns a reference to the node that contains value v
        Returns None if v is not present in the tree
        """
        # TODO
        # Base Case of found
        if v == self.value:
            return self
        # If smaller, search left
        if v < self.value and self._left is not None:
            self._left.find(v)
        # If bigger, search right
        if v > self.value and self._right is not None:
            self._right.find(v)
        # Base Case of unfound
        return None

    def list_in_order(self):
        """
        Returns a sorted list of all the values contained in this node's subtree
        ***Duplicates included***
        """
        # TODO
        left = []
        this = [self.value] * self.counter
        right = []
        if self._left is not None:
            left = self._left.list_in_order()
        if self._right is not None:
            right = self._right.list_in_order()
        return left + this + right

    def remove(self):
        """
        Removes this node from the tree
        Returns a reference to the node that remains
        #   None if removed node is a leaf
        #   child if removed node has only one child
        #   itself if removed node has two children =>
        #        ***removes its successor instead***
        """
        # TODO
        # Case 1: No children (leaf node)
        if self.nb_of_children() == 0:
            # Parent reference reset (no need to do with root)
            if self._parent is not None:
                # self is the left children of its parent
                if self._parent._left == self:
                    self._parent._left = None
                # self is the left children of its parent
                else:
                    self._parent._right = None
            remainder = None

        # Case 2: One child
        elif self.nb_of_children() == 1:
            # Find the child
            if self._left is not None:
                child = self._left
            else:
                child = self._right

            # Parent reference reset (no need to do with root)
            if self._parent is not None:
                # if self is the left children of its parent
                if self._parent._left == self:
                    self._parent._left = child
                # if self is the right children of its parent
                else:
                    self._parent._right = child

            child._parent = self._parent
            remainder = child

        # Case 3: Two children
        else:
            # Find the successor
            successor = self._right
            while successor._left is not None:
                successor = successor._left

            # Replace the value and counter
            self.value = successor.value
            self.counter = successor.counter

            # Remove the successor node and return self
            # The successor has at most 1 child
            successor.remove()
            remainder = self

        return remainder
