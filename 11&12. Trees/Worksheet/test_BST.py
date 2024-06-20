from BST import BinarySearchTree
from TreePrint import *
import random


def main():
    tree = BinarySearchTree()
    for i in range(12):
        tree.add(random.randint(1, 20))
    print(tree.list_in_order())
    print(tree.height())
    pretty_print(tree)
    lvl_order = tree.list_breadth_first()
    print(lvl_order)
    for e in lvl_order:
        print("removing", e)
        tree.remove(e)
        print(tree.list_in_order())
        pretty_print(tree)


main()
