# Copyright 2024 Genghis, 骆可瀚(Luo Kehan), kl4747@nyu.edu

class Employee:
    """Employee Class"""
    
    def __init__(self, name, number):
        self.__name = name
        self.__number = number

    def get_name(self):
        return self.__name

    def get_number(self):
        return self.__number

    def set_name(self, name):
        self.__name = name

    def set_number(self, number):
        self.__number = number


class ProductionWorker(Employee):
    """Production Worker Class, Subclass of Employee Class"""
    
    def __init__(self, name, number, shift, pay_rate):
        super().__init__(name, number)
        self.__shift = shift
        self.__pay_rate = pay_rate

    def get_shift(self):
        if self.__shift == 1:
            return "day shift"
        else:
            return "night shift"

    def get_pay_rate(self):
        return self.__pay_rate

    def set_shift(self, shift):
        self.__shift = shift

    def set_pay_rate(self, pay_rate):
        self.__pay_rate = pay_rate


def main():
    # Prompt user for ProductionWorker data
    name = input("Enter the employee's name: ")
    number = input("Enter the employee's number: ")
    shift = int(input("Enter the shift number (1 for day, 2 for night): "))
    pay_rate = float(input("Enter the hourly pay rate: "))

    # Create a ProductionWorker object
    worker = ProductionWorker(name, number, shift, pay_rate)

    # Display the ProductionWorker information
    print("\nEmployee Information:")
    print(f"Name: {worker.get_name()}")
    print(f"Number: {worker.get_number()}")
    print(f"Shift: {worker.get_shift()}")
    print(f"Hourly Pay Rate: ${worker.get_pay_rate():.2f}")


if __name__ == "__main__":
    main()
