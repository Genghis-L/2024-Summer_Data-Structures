from QuickSort import *
from ShellSort import *


def main():
    import random

    n = 100
    print(f"Length of the List to be sorted: {n}")

    # ShellSort experiment
    total_comparison, total_swap = 0, 0
    for _ in range(5):
        S = [random.randint(0, n) for _ in range(n)]
        comparisons, swaps = shell_sort(S)
        total_comparison += comparisons
        total_swap += swaps
    print(f"Average Comparisons in ShellSort: {total_comparison / 5}")
    print(f"Average Swaps in ShellSort: {total_swap / 5}")

    # QuickSort experiment
    total_comparison, total_swap = 0, 0
    for _ in range(5):
        S = [random.randint(0, n) for _ in range(n)]
        comparisons, swaps = quick_sort(S)
        total_comparison += comparisons
        total_swap += swaps
    print(f"Average Comparisons in QuickSort: {total_comparison / 5}")
    print(f"Average Swaps in QuickSort: {total_swap / 5}")


main()
