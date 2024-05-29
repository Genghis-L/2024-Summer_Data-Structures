# Copyright 2024 Genghis, 骆可瀚(Luo Kehan), kl4747@nyu.edu

# Solution1: basic loop
# Solution2: convert list to set and compare the length, as set() function uses hash table, the time complexity is O(n)


def has_duplicate(list1: list) -> bool:
    """
    remember to mention your runtime as comment!
    # TODO
    My runtime is: O(n^2)

    :param list1: List -- list of integers
    :return: True if list1 has duplicate, return False otherwise.
    """

    ## Solution 1: O(n^2)
    for i in range(len(list1)):
        for j in range(i + 1, len(list1)):
            if list1[i] == list1[j]:
                return True
    return False

    ## Solution 2: O(n)
    # set1 = set(list1)
    # return len(set1) != len(list1)


"""
Note: 
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.

"""


# def main():
#     print(has_duplicate([0, 6, 2, 4, 9]))  # False

#     print(has_duplicate([0, 6, 2, 4, 9, 1, 2]))  # True


# if __name__ == "__main__":
#     main()
