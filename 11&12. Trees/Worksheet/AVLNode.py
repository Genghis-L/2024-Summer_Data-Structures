# Copyright 2024 Genghis, 骆可瀚(Luo Kehan), kl4747@nyu.edu


# Flag Optimization for add() is added as there will be no more than one actual rebalance occurs for each adding
# Flag Optimization for remove() is added as to improve the efficiency


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

    def rebalance(self):
        """A function that rebalance the subtree rooted at self
        Return: new root
        @globvar flag: A flag that shows whether actual rebalance happens for one adding operation
        """
        global flag
        bf = self.balance_factor()
        newRoot = self
        if bf > 1:
            flag = True
            # Left Imbalance
            if self._left.balance_factor() >= 0:
                # Left Outside Case
                newRoot = self.rotate_right()
            else:
                # Left Inside Case
                self._left = self._left.rotate_left()
                newRoot = self.rotate_right()
        elif bf < -1:
            flag = True
            # Right Imbalance
            if self._right.balance_factor() <= 0:
                # Right Outside Case
                newRoot = self.rotate_left()
            else:
                # Right Inside Case
                self._right = self._right.rotate_right()
                newRoot = self.rotate_left()
        return newRoot

    def add(self, v):
        """A function that adds a value v to the subtree rooted at self
        Overwrite the add() in BSTNode for AVLNode
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
                    self._left = self._left.rebalance()
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
                    self._right = self._right.rebalance()

        return newNode

    def remove(self, flag=False):
        """A function that Removes self from the tree
        Overwrite the remove() in BSTNode for AVLNode
        Returns:
        #   None if removed node is a leaf
        #   child if removed node has only one child
        #   itself if removed node has two children => removes its predecessor instead
        @flag: signal whether we have already completed the necesarry traversal back from parent to root's child, specifically designed for two children case
        The root is considered at class AVLTree
        """
        parent = self._parent

        # Case 1: No children (leaf node)
        if self.nb_of_children() == 0:
            # Parent reference reset (no need to do with root)
            if parent is not None:
                # self is the left child of its parent
                if parent._left == self:
                    parent._left = None
                # self is the right child of its parent
                else:
                    parent._right = None

            remainder = None

        # Case 2: One child
        elif self.nb_of_children() == 1:
            # Find the child
            if self._left is not None:
                child = self._left
            else:
                child = self._right

            # Parent reference reset
            if parent is not None:
                # if self is the left child of its parent
                if parent._left == self:
                    parent._left = child
                # if self is the right child of its parent
                else:
                    parent._right = child
            child._parent = parent

            remainder = child

        # Case 3: Two children
        else:
            # Find the predecessor
            predecessor = self._left
            while predecessor._right is not None:
                predecessor = predecessor._right

            # Replace the value and counter
            self.value = predecessor.value
            self.counter = predecessor.counter

            # Remove the predecessor node and return self
            # The predecessor has at most 1 child
            predecessor.remove()
            
            # We do not need to do the backward traverse again for self since we have done it in the recursion of predecessor
            flag = True

            remainder = self

        # Rebalance from parent to the root's child
        # the root is considered at AVLTree
        if not flag:
            curNode = parent
            while curNode is not None and curNode._parent is not None:
                newRoot = curNode.rebalance()
                # Set the reference of parent-to-newRoot
                if newRoot._parent._left == curNode:
                    # If newRoot is the left child
                    newRoot._parent._left = newRoot
                else:
                    # If newRoot is the right child
                    newRoot._parent._right = newRoot
                curNode = newRoot._parent

        return remainder
