# Copyright 2024 Genghis, 骆可瀚(Luo Kehan), kl4747@nyu.edu

# New function gcd() created, all the results are reduced to simpliest fraction


class Fraction:
    def __init__(self, numerator: int = 0, denominator: int = 1):
        self.numerator = numerator
        if denominator != 0:
            self.denominator = denominator
        else:
            raise ZeroDivisionError()

    def __add__(self, other):
        """
        create and return a new Fraction object, which is the sum of self + other.
        DO NOT MODIFY self.

        :param other: Fraction -- the other fraction number.
        :return: Fraction -- a **new** Fraction object, which is the sum of self + other.
        """

        n1 = self.numerator
        n2 = other.numerator
        d1 = self.denominator
        d2 = other.denominator
        result = Fraction(n1 * d2 + n2 * d1, d1 * d2)
        result.reduce()
        return result

    def __iadd__(self, other):
        """
        modify the self Fraction object, which adds other Fraction object value to self.

        :param other: Fraction -- the other fraction number.
        :return: self. The value of self should become the sum of self + other.
        """

        self.numerator = (self + other).numerator
        self.denominator = (self + other).denominator
        return self

    def __sub__(self, other):
        """
        create and return a new Fraction object, which is the subtraction of self - other.
        DO NOT MODIFY self.

        :param other: Fraction -- the other fraction number.
        :return: Fraction -- a **new** Fraction object, which is the subtraction of self - other.
        """

        n1 = self.numerator
        n2 = other.numerator
        d1 = self.denominator
        d2 = other.denominator
        result = Fraction(n1 * d2 - n2 * d1, d1 * d2)
        result.reduce()
        return result

    def __mul__(self, other):
        """
        create and return a new Fraction object, which is the multiplication of self * other.
        DO NOT MODIFY self.

        :param other: Fraction -- the other fraction number.
        :return: Fraction -- a **new** Fraction object, which is the multiplication of self * other.
        """

        n1 = self.numerator
        n2 = other.numerator
        d1 = self.denominator
        d2 = other.denominator
        result = Fraction(n1 * n2, d1 * d2)
        result.reduce()
        return result

    def __eq__(self, other) -> bool:
        """
        Compare if self Fraction object has equal numerical value to the other Fraction object.
        Example: 2/3 == 4/6 --> True
                 2/3 == 2/3 --> True
        If you use the reduce() function here, it is fine.

        :param other: Fraction -- the other fraction number.

        :return: True if the float value of self is equal to other;
                 False if the float value of self is not equal to other.
        """

        self.reduce()
        other.reduce()
        return (
            self.numerator == other.numerator and self.denominator == other.denominator
        )

    def _gcd(self, a: int, b: int) -> int:
        """
        Computes the greatest common divisor (GCD) of two numbers.

        :param a: An integer.
        :param b: Another integer.
        :return: The greatest common divisor of a and b.
        """

        while b != 0:
            a, b = b, a % b
        return a

    def reduce(self):
        """
        Reduces (Simpilifies) the self Fraction object.
        Modifies both self.numerator and self.denominator.
        For example: 12 / 24 --> 1 / 2;  16 / 20 --> 4 / 5

        :return: Nothing.
        """

        gcd = self._gcd(self.numerator, self.denominator)

        self.numerator //= gcd
        self.denominator //= gcd

    def __str__(self):
        """
        Displays the self Fraction object nicely.
        Recommended format:
        Suppose,
        self.numerator = 5
        self.denominator = 6
        Then, should return "5 / 6"

        :return: The string representation of self Fraction object.
        """

        return f"{self.numerator} / {self.denominator}"


"""
Note: 
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.

"""


# def main():
#     x = Fraction(3, 4)
#     y = Fraction(4, 6)
#     print(x)  # 3 / 4
#     print(y)  # 4 / 6
#     print(x + y)  # 34 / 24 or any value that is equal
#     z = x + y
#     print(x * y)  # 12 / 24 or any value that is equal
#     print(x - y)  # 2 / 24 or any value that is equal
#     y.reduce()
#     print(y)  # 2 / 3
#     z.reduce()
#     print(z)  # 17 / 12

#     print(z == Fraction(-17, -12))  # True
#     print(z == Fraction(51, 36))  # True
#     print(z == Fraction(-7, 4))  # False


# if __name__ == "__main__":
#     main()
