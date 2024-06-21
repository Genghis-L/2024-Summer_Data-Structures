class DictionaryADT:

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, item):
        return self.get(item)

    def __delitem__(self, key):
        return self.remove(key)

    """
    Inserts a new key-value pair (k,v) in the dictionary.
    Will be overwritten in implementation
    """

    def put(self, k, v):
        # TODO
        pass

    """
    Looks for a key-value pair (K_i,V_i) whose key matches k in the dictionary.
    Will be overwritten in implementation
    """

    def get(self, k):
        # TODO
        pass

    """
    Looks for a key-value pair (K_i,V_i) whose key matches k in the dictionary.
    Will be overwritten in implementation
    """

    def remove(self, k):
        # TODO
        pass
