import random


def binarySearch(array, element):
    #TODO
    return recursiveBinarySearch(array, 0, len(array) - 1, element)


def recursiveBinarySearch(array, low_index, high_index, element):
    #TODO
    # Base Case
    if low_index > high_index:
        return None

    mid_idx = (low_index + high_index) // 2
    mid_elt = array[mid_idx]

    if mid_elt == element:
        return f"{mid_elt} at {mid_idx}th position"
    elif mid_elt > element:
        return recursiveBinarySearch(array, low_index, mid_idx - 1, element)
    else:
        return recursiveBinarySearch(array, mid_idx + 1, high_index, element)


def main():
    l = []
    for i in range(20):
        l.append(random.randint(1, 99))
    l.sort()
    print(l)
    print(binarySearch(l, l[5]))
    print(binarySearch(l, l[0]))
    print(binarySearch(l, l[19]))
    print(binarySearch(l, 22))


main()
