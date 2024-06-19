# Flag Optimization for add() is added as there will be no more than one actual rebalance occurs for each adding


from BSTNode import *


class AVLNode(BSTNode):
    def __init__(self, value):
        super().__init__(value)

    def balance_factor(self):
        """A function that returns the balance factor of self"""
        lheight, rheight = 0, 0
        if self._left is not None:
            lheight = self._left.height()
        if self._right is not None:
            rheight = self._right.height()
        return lheight - rheight

    def rotate_left(self):
        """A function that does left rotation to the subtree rooted at self
        Return: new root
        """
        # Rotation
        swap = self._right
        self._right = swap._left
        swap._left = self

        # Parent Reassignment
        swap._parent = self._parent
        self._parent = swap
        if self._right is not None:
            self._right._parent = self
        return swap

    def rotate_right(self):
        """A function that does right rotation to the subtree rooted at self
        Return: new root
        """
        # Rotation
        swap = self._left
        self._left = swap._right
        swap._right = self

        # Parent Reassignment
        swap._parent = self._parent
        self._parent = swap
        if self._left is not None:
            self._left._parent = self
        return swap

    def rebalance(self, v):
        """A function that rebalance the subtree rooted at self
        Return: new root
        @globvar flag: A flag that shows whether actual rebalance happens for one adding operation
        """
        global flag
        bf = self.balance_factor()
        new_root = self
        if bf > 1:
            flag = True
            # Left Imbalance
            if v < self._left.value:
                # Left Outside Case
                new_root = self.rotate_right()
            else:
                # Left Inside Case
                self._left = self._left.rotate_left()
                new_root = self.rotate_right()
        elif bf < -1:
            flag = True
            # Right Imbalance
            if v > self._right.value:
                # Right Outside Case
                new_root = self.rotate_left()
            else:
                # Right Inside Case
                self._right = self._right.rotate_right()
                new_root = self.rotate_left()
        return new_root

    def add(self, v):
        """A function that adds a value v to the subtree rooted at self
        Overwrite the add function in BSTNode for AVLNode
        Return: the inserted node containing value v
        @globvar flag: A flag that shows whether actual rebalance happens for one adding operation,
                       if True, then no need to continue traversing back till root for rebalance
        """
        global flag
        if self._parent is None:
            # Initialize flag when self is the root
            flag = False

        # Set the initial value for newNode in each recursion
        newNode = None

        # Duplicate Case
        if self.value == v:
            self.counter += 1
            return self

        if v < self.value:
            if self._left is None:
                # If position is empty, insert directly
                # No need to do rebalance in this Base Case
                newNode = AVLNode(v)
                self._left = newNode
                newNode._parent = self
            else:
                # Otherwise, do recursion on adding and traverse until root's child to do rebalance
                # Flag Optimization added
                self._left.add(v)
                if flag is False:
                    self._left = self._left.rebalance(v)
        else:
            if self._right is None:
                # If position is empty, insert directly
                # No need to do rebalance in this Base Case
                newNode = AVLNode(v)
                self._right = newNode
                newNode._parent = self
            else:
                # Otherwise, do recursion on adding and traverse until root's child to do rebalance
                # Flag Optimization added
                self._right.add(v)
                if flag is False:
                    self._right = self._right.rebalance(v)

        return newNode
