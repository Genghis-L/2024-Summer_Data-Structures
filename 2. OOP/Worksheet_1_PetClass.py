# Copyright 2024 Genghis, 骆可瀚(Luo Kehan), kl4747@nyu.edu

class Pet:
    """Pet Class"""

    def __init__(self, name, type, age) -> None:
        self.__name = name
        self.__animal_type = type
        self.__age = age

    def __str__(self):
        return f"Your pet is: \n(name: {self.__name}, type: {self.__animal_type}, age: {self.__age})"

    def set_name(self, new_name):
        self.__name = new_name

    def set_animal_type(self, new_type):
        self.__animal_type = new_type

    def set_age(self, new_age):
        self.__age = new_age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age


def main():

    name = input("Please input your pet's name: ")
    type = input("Please input your pet's type: ")
    age = int(input("Please input your pet's age: "))

    pet_1 = Pet(name, type, age)

    print(pet_1)


if __name__ == "__main__":
    main()
