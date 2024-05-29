import random


def merge(array1, array2):
    pass ##Replace with completed code


def mergeSort(array):
    pass ##Replace with completed code


def testMerge():
    l1, l2 = [], []
    for i in range(6):
        l1.append(random. randint(1, 99))
        l2.append(random. randint(1, 99))
    l2.append(random. randint(1, 99))
    l2.append(random. randint(1, 99))
    l1.sort()
    l2.sort()
    print(l1)
    print(l2)
    print(merge(l1, l2))

def testMergeSort():
    l = []
    for i in range(23):
        l.append(random. randint(1, 99))
    print(l)
    l2 = l[:]
    l2.sort()
    print(l2)
    l2 = mergeSort(l)
    print(l2)


def main():
##    testMerge()    
##    testMergeSort()    

main()
