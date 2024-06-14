# Copyright 2024 Genghis, 骆可瀚(Luo Kehan), kl4747@nyu.edu

# Question: How to write a recursive solution to the function __setitem__()?

import random


class Item:
    def __init__(self, k, v):
        self._key = k
        self._value = v

    def __eq__(self, other):
        return self._key == other._key  # compare items based on their keys

    def __ne__(self, other):
        return not (self == other)  # opposite of __eq__

    def __lt__(self, other):
        return self._key < other._key  # compare items based on their keys


class CuckooHashTable:
    def __init__(self):
        self._size = 0
        self._maxsize = 11
        self._array1 = [None] * self._maxsize
        self._array2 = [None] * self._maxsize
        self._random1 = random.random()
        self._random2 = random.random()

    def _hash1(self, k):
        return hash((k, self._random1)) % self._maxsize

    def _hash2(self, k):
        return hash((k, self._random2)) % self._maxsize

    def __getitem__(self, k):
        """given a key k, return the value associated with k
        use hash1/hash2 to compute the index
        raise KeyError if k does not exist in the table
        """
        # TODO
        # Get the item's hash idx in two hash tables
        idx1 = self._hash1(k)
        idx2 = self._hash2(k)

        # Check hash table 1
        if self._array1[idx1] is not None and self._array1[idx1]._key == k:
            return self._array1[idx1]._value
        # Check hash table 2
        if self._array2[idx2] is not None and self._array2[idx2]._key == k:
            return self._array2[idx2]._value

        raise KeyError(f"The key {k} does not exist in the table")

    def __setitem__(self, k, v):
        """if key k exists in either array, modify associated value to v
        if key k does not exist in both arrays, insert (k, v) into table as a new class Item
        if there's a cycle, rehash the table
        Hint: You may want to use the _resize function for cycles
        """
        # TODO
        # By thoery, insertions succeed in expected constant time, as long as the load factor is below 50%. -- from Wikipedia
        # Though this initial resizing process may not be very useful to reduce time by my test in practice
        if self._size > self._maxsize // 2:
            self._resize()

        item = Item(k, v)
        inserted_item = item  # Track the initial key to detect cycles
        while True:
            # Check hash table 1
            idx1 = self._hash1(item._key)
            # Set the item if position is empty
            if self._array1[idx1] is None:
                self._array1[idx1] = item
                self._size += 1
                return
            # Otherwise, let new item take place of the position and look new position for the original item
            self._array1[idx1], item = item, self._array1[idx1]

            # Check hash table 2
            idx2 = self._hash2(item._key)
            # Set the item if position is empty
            if self._array2[idx2] is None:
                self._array2[idx2] = item
                self._size += 1
                return
            # Otherwise, let new item take place of the position and look new position for the original item
            self._array2[idx2], item = item, self._array2[idx2]

            # If the inserted item has been displaced from array2, i.e., the inserted item has no place to insert
            # Then it means we encounter a circle, so break to resize and restart
            if item is inserted_item:
                break

        # If there is a circle occurred, resize/rehash the table and do insertion from start
        self._resize()
        self.__setitem__(k, v)

    def __delitem__(self, k):
        """given a key k, set the corresponding index in self._array1 or self._array2 to None
        raise KeyError if k does not exist in the table
        """
        # TODO
        # Get the item's hash idx in two hash tables
        idx1 = self._hash1(k)
        idx2 = self._hash2(k)

        # Check hash table 1
        if self._array1[idx1] is not None and self._array1[idx1]._key == k:
            self._array1[idx1] = None
            self._size -= 1
            return
        # Check hash table 2
        if self._array2[idx2] is not None and self._array2[idx2]._key == k:
            self._array2[idx2] = None
            self._size -= 1
            return

        raise KeyError(f"The key {k} does not exist in the table")

    def _resize(self):
        """double the size of self._array1, self._array2.
        also self._maxsize
        Remember to rehash all the old (key, value) pairs!
        """
        # TODO
        # Get a list of all the old items
        items = list(self.items())
        # Initialize the new hash tables
        self._maxsize *= 2
        self._array1 = [None] * self._maxsize
        self._array2 = [None] * self._maxsize
        self._size = 0
        # Put old items into the new hash tables
        for item in items:
            self.__setitem__(item._key, item._value)

    def __len__(self):
        # TODO
        return self._size

    def __contains__(self, k):
        """return True if key k exists in the table
        return False otherwise
        """
        # TODO
        try:
            self.__getitem__(k)
            return True
        except KeyError:
            return False

    def __iter__(self):
        """same as keys(self)"""
        return self.keys()

    def keys(self):
        """yield an generator of keys in table"""

        def keys_generator():
            items = self.items()
            for item in items:
                yield item._key

        return keys_generator()

    def values(self):
        """yield an generator of values in table"""

        def values_generator():
            items = self.items()
            for item in items:
                yield item._value

        return values_generator()

    def items(self):
        """yield an generator of Items in table"""

        def items_generator():
            for i in self._array1:
                if i is not None:
                    yield i
            for i in self._array2:
                if i is not None:
                    yield i

        return items_generator()


# def main():
#     table = CuckooHashTable()
#     for i in range(200):
#         # Tests __setitem__, insert 0 ~ 199. _resize() also need to work correctly.
#         table[i] = "happy_coding"

#     print(len(table))  # Tests __len__, should be 200.
#     # print(len(table._array1))

#     for j in range(195):  # Tests __delitem__, delete 0 ~ 194
#         del table[j]

#     print(len(table))  # Tests __len__, should be 5.

#     for j in table.items():  # Tests items()
#         print(j._key)  # 195, 196, 197, 198, 199 left in table

#     print(table[196])  # Tests __getitem__
#     # Should print "happy_coding"


# if __name__ == "__main__":
#     # for _ in range(1000):
#     main()
