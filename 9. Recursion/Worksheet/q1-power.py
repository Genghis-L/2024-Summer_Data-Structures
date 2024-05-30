##  Computes the value of (x**n) recursively
#   x is any numeric value (int or float)
#   n is a positive integer value
def power(x, n):
    #TODO
    if n == 1:
        return x
    return x * power(x, n - 1)


def main():
    print(power(-2, 4))
    print(power(4, 3))
    print(power(2, 12))
    print(power(3.2, 4))


main()
