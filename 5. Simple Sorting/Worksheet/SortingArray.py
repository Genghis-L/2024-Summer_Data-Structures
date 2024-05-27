class SortingArray:

    def __init__(self, capacity):
        self.__capacity = capacity
        self.__array = [None] * capacity
        self.__nb_elts = 0

    # Returns the number of elements stored in the array.
    def get_size(self):
        return self.__nb_elts

    # Inserts a new element in the array.
    def insert(self, element):
        if self.__nb_elts == self.__capacity:
            print("Array is full")
        else:
            self.__array[self.__nb_elts] = element
            self.__nb_elts += 1

    # Displays the data items in the array
    def display(self):
        print(self.__nb_elts, "values")
        print("[ ", end="")
        for i in range(self.__nb_elts):
            print(self.__array[i], end=" ")
        print("]")

    # Swaps two data items in the array
    # The item initially at position index1 ends up at position index2
    # The item initially at position index2 ends up at position index1
    def swap(self, array, index1, index2):
        v = array[index1]
        array[index1] = array[index2]
        array[index2] = v

    # Sorts the data from this array with the BUBBLE sorting algorithm
    # Returns a tuple containing a new list with all of the array data in increasing order, number of comparisons, number of swaps
    # IMPORTANT: The attribute '__array' must remained unordered!
    #            => Carry out the sorting in the copy 'sorted_array'
    def bubbleSort(self):
        # Stable since we do not change the relative order of duplicates
        sorted_array = self.__array[:]  # copy of the array to be sorted
        nb_comps = 0  # Number of comparisons
        nb_swaps = 0  # Number of swaps

        # TODO
        n = len(sorted_array)

        for i in range(n):
            swapped = False

            for j in range(n - i - 1):
                # Optimized, but still O(n) time complexity per loop
                nb_comps += 1
                if sorted_array[j] > sorted_array[j + 1]:
                    self.swap(sorted_array, j, j + 1)
                    nb_swaps += 1
                    swapped = True

            if not swapped:
                break

        return sorted_array, nb_comps, nb_swaps

    # Sorts the data from this array with the SELECTION sorting algorithm
    # Returns a tuple containing a new list with all of the array data in increasing order, number of comparisons, number of swaps
    # IMPORTANT: The attribute '__array' must remained unordered!
    #            => Carry out the sorting in the copy 'sorted_array'
    def selectionSort(self):
        # Not stable in the usual case, though we can modify. Counter-example: 5(1),5(2),1 -> 1,5(2),5(1)
        sorted_array = self.__array[:]  # copy of the array to be sorted
        nb_comps = 0  # Number of comparisons
        nb_swaps = 0  # Number of swaps

        # TODO
        n = len(sorted_array)

        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                nb_comps += 1
                if sorted_array[j] < sorted_array[min_idx]:
                    # To make it stable, we can add another condition here: (sorted_array[j] == sorted_array[min_idx] and j < min_idx)
                    min_idx = j

            if min_idx != i:  # Otherwise, no need to swap
                self.swap(sorted_array, i, min_idx)
                nb_swaps += 1

        return sorted_array, nb_comps, nb_swaps

    # Sorts the data from this array with the INSERTION sorting algorithm
    # Returns a tuple containing a new list with all of the array data in increasing order, number of comparisons, number of swaps
    # IMPORTANT: The attribute '__array' must remained unordered!
    #            => Carry out the sorting in the copy 'sorted_array'
    def insertionSort(self):
        # Stable since we do not change the relative order of duplicates
        sorted_array = self.__array[:]  # copy of the array to be sorted
        nb_comps = 0  # Number of comparisons
        nb_swaps = 0  # Number of swaps

        # TODO
        n = len(sorted_array)

        for i in range(1, n):  # No need to look at the first one
            idx = i
            for j in range(i - 1, -1, -1):
                # Using swap one by one from end to front to achieve insertion, it is equivalent to using reassignment as they are all O(n) time complexity per loop
                nb_comps += 1
                if sorted_array[j] > sorted_array[idx]:
                    self.swap(sorted_array, j, idx)
                    idx = j
                    nb_swaps += 1
                else:  # We can break if we see one that is not greater
                    break

        return sorted_array, nb_comps, nb_swaps
