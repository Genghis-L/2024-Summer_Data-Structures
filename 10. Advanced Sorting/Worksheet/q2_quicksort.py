# A swap function is added to see the swapping more clearly


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def medianOfThree(array, a, b):
    """Determines the median of three values in a portion of the array.
    Considers three values in the portion: first(a), last(b) and middle position.

    Finally puts the median value at array[b] to make it ready for partition.

    @array: a python list
    @a: beginning index of the portion
    @b: ending index of the portion

    @return: Nothing
    """
    # TODO
    global comparisons, swaps

    mid = (a + b) // 2

    # Order array[a], array[b] and array[mid]
    if array[a] > array[mid]:
        swap(array, a, mid)
        swaps += 1
    if array[a] > array[b]:
        swap(array, a, b)
        swaps += 1
    if array[mid] > array[b]:
        swap(array, mid, b)
        swaps += 1

    comparisons += 3

    # Swap the median value to the end: array[b]
    swap(array, mid, b)


def inplace_quick_sort(array, a, b):
    global comparisons, swaps
    """Sort the list from array[a] to array[b] inclusive,
       using the quick-sort algorithm."""
    # TODO
    # Base Case: If there is only one elmt, no need to swap
    if a >= b:
        return

    # Use median of three method to find pivot and put it to the array end: array[b]
    medianOfThree(array, a, b)
    pivot = array[b]
    i = a  # left pointer
    j = b - 1  # right pointer

    while True:
        # while until we find the two elmts need to be swapped
        while i <= j and array[i] < pivot:
            comparisons += 1
            i += 1
        while i <= j and array[j] > pivot:
            comparisons += 1
            j -= 1

        if i <= j:
            # If these two elmts are valid to swap
            swap(array, i, j)
            swaps += 1
            i += 1
            j -= 1
        else:
            # Otherwise, we break the outer while and proceed
            break

    # swap the left pointer and the pivot
    swap(array, i, b)
    swaps += 1
    # one partition is done, pivot is now at correct position

    # Do recursion on the left and the right side
    inplace_quick_sort(array, a, i - 1)
    inplace_quick_sort(array, i + 1, b)


def quick_sort(array):
    inplace_quick_sort(array, 0, len(array) - 1)


def main():
    global comparisons, swaps
    comparisons, swaps = 0, 0

    import random

    S = [random.randint(-999, 999) for _ in range(1000)]

    quick_sort(S)
    print("Is S sorted???", S == sorted(S))
    print("comparisons:", comparisons)
    print("swaps:", swaps)


main()
