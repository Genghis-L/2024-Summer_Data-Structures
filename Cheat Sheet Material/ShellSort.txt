def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def inplace_shell_sort(array):
    global comparisons, swaps
    gap_list = []

    n = len(array)

    # Create the gap_list by Knuth's 1973 suggetstion
    i = 1
    while i < n:
        gap_list.append(i)
        i = i * 3 + 1

    # Reverse the gap_list for convenient traverse
    gap_list.reverse()

    for gap in gap_list:
        # Starting from the second gap to do Insertion Sort to each column (elmts in the same position in each gap)
        for i in range(gap, n):
            temp = array[i]
            j = i
            while j >= gap:
                comparisons += 1
                if array[j - gap] <= temp:
                    break
                swap(array, j, j - gap)
                swaps += 1
                j -= gap
            array[j] = temp


def shell_sort(array):
    """Do the shell sort and return (comparisons, swaps)"""
    global comparisons, swaps
    comparisons, swaps = 0, 0
    inplace_shell_sort(array)
    return comparisons, swaps
