# Copyright 2024 Genghis, 骆可瀚(Luo Kehan), kl4747@nyu.edu


# Problem 1
class Student:
    """Student Class"""

    def __init__(self, name, age, gpa) -> None:
        self.name = name
        self.age = age
        self.__gpa = gpa

    def get_gpa(self):
        return self.__gpa

    def set_gpa(self, new_gpa):
        self.__gpa = new_gpa


def main_1():
    a = Student("Charlie", 18, 4.0)
    print(a.get_gpa())
    a.set_gpa(3.9)
    print(a.get_gpa())


# Problem 2
class Pizza:
    """Pizza Class"""

    def __init__(self, price) -> None:
        self.price = price

    def __iadd__(self, other):
        self.price += other.price
        return self

    def __add__(self, other):
        new_pizza = Pizza(self.price)
        new_pizza += other
        return new_pizza

    def __str__(self) -> str:
        return "the price is " + str(self.price)


def main_2():
    pizza1 = Pizza(5)
    pizza2 = Pizza(6)
    pizza1 += pizza2
    print(pizza1)
    pizza3 = pizza1 + pizza2
    print(pizza3)


# Problem 3
class Tree:
    """Tree Class"""

    def __init__(self, name, age) -> None:
        self._name = name
        self._age = age

    def get_name(self):
        return self._name


class Palm(Tree):
    """Palm Tree Subclass"""

    def __init__(self, name, age, color) -> None:
        super().__init__(name, age)
        self._color = color

    def get_color(self):
        return self._color


def main_3():
    palm1 = Palm("Lucky", 30, "green")
    print(palm1.get_name())
    print(palm1.get_color())
    tree1 = Tree("Funny", 20)
    print(tree1.get_name())
    # print(tree1.get_color()) # AttributeError


if __name__ == "__main__":

    main_1()

    main_2()

    main_3()
