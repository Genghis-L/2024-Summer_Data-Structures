import random


def merge(array1, array2):
    # array1 & array2 are sorted
    # TODO
    # Create a new memory as the result of the merged array
    merged = []
    i = j = 0
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            merged.append(array1[i])
            i += 1
        else:
            merged.append(array2[j])
            j += 1

    # Put left-overs in array1 or array2 (only one has) into the merged array
    merged.extend(array1[i:] + array2[j:])
    return merged


def mergeSort(array):
    # TODO
    # Base Case
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left = mergeSort(array[:mid])
    right = mergeSort(array[mid:])
    return merge(left, right)


def testMerge():
    l1, l2 = [], []
    for i in range(6):
        l1.append(random.randint(1, 99))
        l2.append(random.randint(1, 99))
    l2.append(random.randint(1, 99))
    l2.append(random.randint(1, 99))
    l1.sort()
    l2.sort()
    print(l1)
    print(l2)
    print(merge(l1, l2))


def testMergeSort():
    l = []
    for i in range(23):
        l.append(random.randint(1, 99))
    print(l)
    l2 = l[:]
    l2.sort()
    print(l2)
    l2 = mergeSort(l)
    print(l2)


def main():
    testMerge()
    testMergeSort()


main()
