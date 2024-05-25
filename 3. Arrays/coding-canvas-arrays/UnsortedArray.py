class UnsortedArray():

    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * capacity
        self.nb_elts = 0

    # Returns the number of elements stored in the array.
    def get_size(self):
        return self.nb_elts

    # Inserts a new element in the array.
    # Displays error notification if the array is already at full capacity.
    def insert(self, element):
        #TODO


    # Removes an element from the array.
    # Displays error notification if the deleted value is not in the array.
    def delete(self, element):
        #TODO
        #HINT: start by finding the index of the value to remove


    # Returns the element at a given position in the array.
    # Returns None if there is no element yet at this position.
    def getElementAt(self, index):
        #TODO

    # Uses LINEAR search to find the position of an element in the array.
    # Returns None if the searched value is not in the array.
    def find(self, element):
        #TODO


    def display(self):
        print(self.nb_elts, 'values')
        print("[ ", end='')
        for i in range(self.nb_elts):
            print(self.array[i], end=' ')
        print("]")
