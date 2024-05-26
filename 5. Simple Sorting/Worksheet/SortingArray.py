class SortingArray():

    def __init__(self, capacity):
        self.__capacity = capacity
        self.__array = [None] * capacity
        self.__nb_elts = 0

    # Returns the number of elements stored in the array.
    def get_size(self):
        return self.__nb_elts

    # Inserts a new element in the array.
    def insert(self, element):
        if (self.__nb_elts == self.__capacity):
            print("Array is full")
        else:
            self.__array[self.__nb_elts] = element
            self.__nb_elts += 1


    # Displays the data items in the array
    def display(self):
        print(self.__nb_elts, 'values')
        print("[ ", end='')
        for i in range(self.__nb_elts):
            print(self.__array[i], end=' ')
        print("]")


    # Swaps two data items in the array
    # The item initially at position index1 ends up at position index2
    # The item initially at position index2 ends up at position index1
    def swap(self, array, index1, index2):
        v = array[index1]
        array[index1] = array[index2]
        array[index2] = v


    # Sorts the data from this array with the BUBBLE sorting algorithm
    # Returns a new list with all of the array data in increasing order
    # IMPORTANT: The attribute '__array' must remained unordered!
    #            => Carry out the sorting in the copy 'sorted_array'
    def bubbleSort(self):
        sorted_array = self.__array[:]      #copy of the array to be sorted
        nb_comps = 0                        #Number of comparisons
        nb_swaps = 0                        #Number of swaps

        #TODO
        
        return sorted_array, nb_comps, nb_swaps


    # Sorts the data from this array with the SELECTION sorting algorithm
    # Returns a new list with all of the array data in increasing order
    # IMPORTANT: The attribute '__array' must remained unordered!
    #            => Carry out the sorting in the copy 'sorted_array'
    def selectionSort(self):
        sorted_array = self.__array[:]      #copy of the array to be sorted
        nb_comps = 0                        #Number of comparisons
        nb_swaps = 0                        #Number of swaps

        #TODO

        return sorted_array, nb_comps, nb_swaps


    # Sorts the data from this array with the INSERTION sorting algorithm
    # Returns a new list with all of the array data in increasing order
    # IMPORTANT: The attribute '__array' must remained unordered!
    #            => Carry out the sorting in the copy 'sorted_array'
    def insertionSort(self):
        sorted_array = self.__array[:]      #copy of the array to be sorted
        nb_comps = 0                        #Number of comparisons
        nb_swaps = 0                        #Number of swaps
        
        #TODO

        return sorted_array, nb_comps, nb_swaps
