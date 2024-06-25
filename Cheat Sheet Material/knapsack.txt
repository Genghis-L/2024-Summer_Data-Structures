# Copyright 2024 Genghis, 骆可瀚(Luo Kehan), kl4747@nyu.edu

# Recursion on Position


import copy


def knapsack_driver(capacity, weights):
    """
    @capacity: positive integer. the value we are summing up to.
    @weights:  list of positive integers.

    ### Friendly tip: This function can't solve the problem,
    ### you need more parameters to pass information between recursive functions.
    ### So, define another function!! Return the result from your new function!!

    @return: List of all combinations that can add up to capacity.
    """

    def knapsack(capacity, weights, position, result, curCast):
        # Base Case 1: If we find one valid cast, append it to result and return
        if capacity == 0:
            result.append(curCast[:])
            return
        # Base Case 2: If we exceed the capacity or we reach the end of weights, return
        if capacity < 0 or position >= len(weights):
            return

        # Include the current weight
        curCast.append(weights[position])
        knapsack(capacity - weights[position], weights, position + 1, result, curCast)
        curCast.pop()
        # Exclude the current weight and proceed
        knapsack(capacity, weights, position + 1, result, curCast)

    result = []
    knapsack(capacity, weights, 0, result, [])
    return result


# def main():
#     casts = [1, 2, 8, 4, 9, 1, 4, 5]
#     # order does not matter, inner values order doesn't matter either.
#     # actual_result = [[9, 5], [9, 1, 4], [4, 1, 4, 5], [4, 9, 1], [8, 1, 5], [2, 8, 4], [2, 8, 4], [1, 9, 4], [1, 4, 4, 5], [1, 4, 9], [1, 8, 5], [1, 8, 1, 4], [1, 8, 4, 1]]
#     my_result = knapsack_driver(14, casts)
#     print(my_result)

#     # actual_result.sort()
#     # my_result.sort()
#     # print(actual_result == my_result)


# if __name__ == "__main__":
#     main()
