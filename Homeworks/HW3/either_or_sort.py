# Copyright 2024 Genghis, 骆可瀚(Luo Kehan), kl4747@nyu.edu


import random


def either_or_sort(array):
    """EitherOr sort arranges all of the zeros in array at the front, before all of the ones.
    It must perform the sorting in-place, and its complexity must be in O(N).
    @array: the python list being sorted
    """
    # TODO
    left, right = 0, len(array) - 1
    while left < right:
        # If array[left] is 0, proceed left
        if array[left] == 0:
            left += 1
        # If array[left] is 1, proceed right
        elif array[right] == 1:
            right -= 1
        # If array[left] is 1 and array[right] is 0, swap and proceed
        else:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1


# def main():
#     array = []
#     for i in range(20):
#         array.append(random.randint(0, 1))

#     print("Before sorting:")
#     print(array)
#     either_or_sort(array)
#     print("After sorting:")
#     print(array)
#     print(array == sorted(array))


# if __name__ == "__main__":
#     main()
