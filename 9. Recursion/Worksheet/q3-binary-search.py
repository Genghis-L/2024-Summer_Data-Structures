import random

def binarySearch(array, element):
    pass ##Replace with completed code

def recursiveBinarySearch(array, low_index, high_index, element):
    pass ##Replace with completed code

def main():
    l = []
    for i in range(20):
        l.append(random. randint(1, 99))
    l.sort()
    print(l)
    print(binarySearch(l, l[5]))
    print(binarySearch(l, l[0]))
    print(binarySearch(l, l[19]))
    print(binarySearch(l, 22))

main()
