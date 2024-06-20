from AVLTree import *
from TreePrint import *
import random

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