comparisons = 0
swaps = 0

def medianOfThree(array, a, b):
    ''' Determines the median of three values in a portion of the array S. 
        Considers three values in the portion: first(a), last(b) and middle position.
        
        Finally puts the median value at S[b] to make it ready for partition.

        @S: a python list
        @a: beginning index of the portion
        @b: ending index of the portion

        @return: Nothing
    '''
    pass



def inplace_quick_sort(array, a, b):
    global comparisons
    global swaps
    """Sort the list from array[a] to array[b] inclusive,
       using the quick-sort algorithm."""
    pass

def quick_sort(array):
    inplace_quick_sort(array, 0, len(array) - 1)    


def main():
    import random
    S = []
    for i in range(1000):
        S.append(random.randint(-999, 999))

    print(S)
    inplace_quick_sort(S)
    print(S)
    print("Is S sorted???", S == sorted(S))
    print("comparisons:", comparisons)
    print("swaps:", swaps)
main()
