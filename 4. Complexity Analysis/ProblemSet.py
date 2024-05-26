# Problem 5, Q2

import random

N = 100
F = random.randint(1, 100)

# Find the lower and upper bound
i = 1
while not (2 ** (i - 1) <= F <= 2**i):
    i += 1

bot = 2 ** (i - 1)
top = min(2**i, N)

# Binary Search
while bot <= top:
    mid = (bot + top) // 2
    if F < mid:
        top = mid - 1
    elif F > mid:
        bot = mid + 1
    else:
        break

print(mid == F)  # True
