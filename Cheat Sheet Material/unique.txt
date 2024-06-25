# Copyright 2024 Genghis, 骆可瀚(Luo Kehan), kl4747@nyu.edu

# similar idea as Merge Sort


def unique(s):
    """
    :param s: List[Any] -- list of values.
    :return: True if all values within s are unique.
             False otherwise.
    """
    # Base case: an empty list or a single-element list is unique
    if len(s) <= 1:
        return True

    # Split the list into two halves
    mid = len(s) // 2
    left = s[:mid]
    right = s[mid:]

    # Check for duplicates between left and right
    for elt in left:
        if elt in right:
            return False

    # Both halves must be unique
    return unique(left) and unique(right)


# def main():
#     print(unique([1, 7, 6, 5, 4, 3, 1]))  # False
#     print(unique([9, 4, 3, 2, 1, 8]))  # True
#     print(unique(["9", [], 4, 3, 2, 1, 8]))  # True


# if __name__ == "__main__":
#     main()
