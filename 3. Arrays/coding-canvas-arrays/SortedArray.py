from UnsortedArray import UnsortedArray

class SortedArray(UnsortedArray):

    def __init__(self, capacity):
        super().__init__(capacity)


    # Inserts a new element in the array; the array remains sorted after insertion.
    # Displays error notification if the array is already at full capacity.
    def insert(self, element):
        #TODO


    # Uses BINARY search to find the position of an element in the array.
    # Returns None if the searched value is not in the array.
    def find(self, element):
        #TODO


    def display(self):
        print(self.nb_elts, 'values')
        print("[ ", end='')
        for i in range(self.nb_elts):
            print(self.array[i], end=' ')
        print("]")
