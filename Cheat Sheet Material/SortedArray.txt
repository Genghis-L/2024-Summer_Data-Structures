from UnsortedArray import UnsortedArray


class SortedArray(UnsortedArray):
    """A class for a sorted array (from smallest to largest)"""

    def __init__(self, capacity):
        super().__init__(capacity)

    # Inserts a new element in the array; the array remains sorted after insertion.
    # Displays error notification if the array is already at full capacity.
    def insert(self, element):
        # TODO

        if self.nb_elts == self.capacity:
            print("The max capacity has been reached.")
            return

        # Find
        idx = self.nb_elts
        for i in range(self.nb_elts):
            if element <= self.array[i]:
                idx = i
                break

        # Shift
        for j in range(self.nb_elts, idx, -1):
            self.array[j] = self.array[j - 1]

        self.array[idx] = element
        self.nb_elts += 1

    # Uses BINARY search to find the position of an element in the array.
    # Returns None if the searched value is not in the array.
    def find(self, element):
        # TODO

        # Solution 1: While loop
        bottom = 0
        top = self.nb_elts - 1
        while bottom <= top:
            mid = (bottom + top) // 2
            if self.array[mid] < element:
                bottom = mid + 1
            elif self.array[mid] > element:
                top = mid - 1
            else:  # Find the element
                return mid

        return None

        # # Solution 2: Recursion
        # def _binary_search(element, bottom, top):
        #     if bottom > top:
        #         return None
        #     mid = (bottom + top) // 2
        #     if self.array[mid] < element:
        #         return _binary_search(element, mid + 1, top)
        #     elif self.array[mid] > element:
        #         return _binary_search(element, bottom, mid - 1)
        #     else:
        #         return mid
        # return _binary_search(element, 0, self.nb_elts - 1)

    def display(self):
        print(self.nb_elts, "values")
        print("[ ", end="")
        for i in range(self.nb_elts):
            print(self.array[i], end=" ")
        print("]")
