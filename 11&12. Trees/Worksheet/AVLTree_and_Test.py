# Copyright 2024 Genghis, 骆可瀚(Luo Kehan), kl4747@nyu.edu


from BinarySearchTree import *
from AVLNode import *
from BSTPrint import *
import random


class AVLTree(BinarySearchTree):
    def __init__(self):
        super().__init__()

    def add(self, v):
        """A function that adds a value v to self
        Overwrite the add function in BST for AVL Tree
        Return: the inserted node
        """
        if self.is_empty():
            # Insert directly in an empty tree
            newNode = AVLNode(v)
            self._root = newNode
        else:
            newNode = self._root.add(v)
            # Do rebalance for the root, which is not covered in AVLNode
            self._root = self._root.rebalance()
        return newNode

    def remove(self, v):
        """A function that removes a value v from self
        # Skip node removal if
        #       (a) value doesn't occur in the tree
        #       (b) counter is higher than 1 (decrement counter)
        Return: a reference to the node containing v; None if no such node found
        (we have not used this return yet)
        """
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
            # Ensure the root is rebalanced
            if self._root is not None:
                self._root = self._root.rebalance()
        # Regular case
        else:
            n.remove()
            # Ensure the root is rebalanced
            if self._root is not None:
                self._root = self._root.rebalance()
        return n


def avl_tree_test():
    tree = AVLTree()
    for i in range(15):
        # new_value = random.randint(1, 99)
        # Worst Case
        new_value = i
        print("Adding", new_value)
        tree.add(new_value)
        pretty_print(tree)

    for i in tree.list_breadth_first():
        value = i
        print("Deleting", value)
        tree.remove(value)
        pretty_print(tree)


avl_tree_test()
