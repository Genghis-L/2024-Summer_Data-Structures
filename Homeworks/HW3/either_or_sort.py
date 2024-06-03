import random

'''
What is the best-case runtime complexity of Comb sort?

Answer:
TODO
'''


def either_or_sort(array):
    """ EitherOr sort arranges all of the zeros in array at the front, before all of the ones.
        It must perform the sorting in-place, and its complexity must be in O(N).
        @array: the python list being sorted
    """
    pass


def main():
    array = []
    for i in range(20):
        array.append(random.randint(0, 1))

    print("Before sorting:")
    print(array)
    either_or_sort(array)
    print("After sorting:")
    print(array)


if __name__ == "__main__":
    main()
