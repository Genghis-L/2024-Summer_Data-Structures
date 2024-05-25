# Copyright 2024 Genghis, 骆可瀚(Luo Kehan), kl4747@nyu.edu

# Dynamic Programming used to trade space for time


def buy_two_items(credit, list1):
    """
    @credit: integer, you want to spend this total amount, exactly.
    @list1: list of integers.

    remember to mention your runtime as comment!
    # TODO
    My runtime is: O(n)

    @return: a tuple of two integers. They should sum up to credit. (Order doesn't matter)
    """
    memory_lst = []

    for value in list1:
        complement = credit - value
        if complement in memory_lst:
            return (complement, value)
        memory_lst.append(value)


"""
Note: 
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.

"""


# def main():
#     print(buy_two_items(200, [150, 24, 79, 50, 88, 345, 3]))
#     print(buy_two_items(295, [678, 227, 764, 37, 956, 982, 118, 212, 177, 597, 519, 968, 866, 121, 771, 343, 561]))


# if __name__ == '__main__':
#     main()
