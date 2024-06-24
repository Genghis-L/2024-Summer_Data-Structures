from random import randrange  # used to pick MAD parameters
from KVItem import KVItem
from DictionaryADT import DictionaryADT


class ChainHashtable(DictionaryADT):
    """
    A ChainHashtable (CHt) stores key-value (KV) items: object instances from class KVItem.
    It uses Python lists to chain all KV items whose hashed key values are the same.
    The capacity represents the total number of possible hash values, and therefore
    the number of bucket lists.
    The table is the list of all bucket lists.
    The size gives the total number of KV items in the CHt.
    """

    def __init__(self, capacity):
        self._cap = capacity
        self._table = []
        for i in range(self._cap):
            self._table.append([])
        self._size = 0

    def __len__(self):
        return self._size

    def _hash_function(self, k):
        h = hash(k) % self._cap
        return h

    def __contains__(self, k):
        h = self._hash_function(k)
        for item in self._table[h]:
            if k == item._key:
                return True
        return False

    def __iter__(self):
        self._index = 0
        self._bucket_index = 0
        return self

    def __next__(self):
        if self._bucket_index >= self._cap:
            raise StopIteration
        else:
            bucket = self._table[self._bucket_index]
            k = bucket[self._index]
            self._index += 1
            if self._index >= len(bucket):
                self._bucket_index += 1
                self._index = 0
            return k._key

    def __str__(self):
        s = "[\n"
        for l in self._table:
            for item in l:
                s += str(item)
            s += "\n"
        s += "]"
        return s

    def items(self):
        for bucket in self._table:
            for item in bucket:
                yield item._key, item._value

    """
    Inserts a new KV item in the CHt.
    """

    def put(self, k, v):
        # TODO
        # Compute the hash index and find the bucket
        hidx = self._hash_function(k)
        bucket = self._table[hidx]

        # Case of key exists, replace the value
        for item in bucket:
            if item._key == k:
                item._value = v
                return

        # Case of key does not exist
        new_item = KVItem(k, v)
        bucket.append(new_item)
        self._size += 1

    """
    Looks for a KV item whose key matches k in the CHt.
    Returns the value of the item if found in the CHt, None otherwise.
    """

    def get(self, k):
        # TODO
        # Compute the hash index and find the bucket
        hidx = self._hash_function(k)
        bucket = self._table[hidx]

        for item in bucket:
            if item._key == k:
                return item._value
        return None

    """
    Looks for a KV item whose key matches k and removes it from the CHt.
    Returns the value of the item if found and removed from the CHt, None otherwise.
    """

    def remove(self, k):
        # TODO
        # Compute the hash index and find the bucket
        hidx = self._hash_function(k)
        bucket = self._table[hidx]

        for idx, item in enumerate(bucket):
            if item._key == k:
                rem_item = bucket.pop(idx)
                self._size -= 1
                return rem_item._value
        return None

    """
    Deletes all the values in the CHt.
    """

    def clear(self):
        for l in self._table:
            del l[:]
        self._size = 0
