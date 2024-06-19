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
            self._root = self._root.rebalance(v)
        return newNode


def avl_tree_test():
    tree = AVLTree()
    for i in range(15):
        # new_value = random.randint(1, 99)
        # Worst Case
        new_value = i
        print("Adding", new_value)
        tree.add(new_value)
        pretty_print(tree)


avl_tree_test()
