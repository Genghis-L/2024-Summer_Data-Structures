# Copyright 2024 Genghis, 骆可瀚(Luo Kehan), kl4747@nyu.edu

from Worksheet_5_Employee_and_ProductionWorker_Classes import *


class ShiftSupervisor(Employee):
    """ShiftSupervisor Class, Subclass of Employee Class"""

    def __init__(self, name, number, annual_salary, annual_bonus):
        super().__init__(name, number)
        self.__annual_salary = annual_salary
        self.__annual_bonus = annual_bonus

    def get_annual_salary(self):
        return self.__annual_salary

    def get_annual_bonus(self):
        return self.__annual_bonus

    def set_annual_salary(self, annual_salary):
        self.__annual_salary = annual_salary

    def set_annual_bonus(self, annual_bonus):
        self.__annual_bonus = annual_bonus


def main():
    # Prompt user for ShiftSupervisor data
    name = input("Enter the shift supervisor's name: ")
    number = input("Enter the shift supervisor's number: ")
    annual_salary = float(input("Enter the annual salary: "))
    annual_bonus = float(input("Enter the annual production bonus: "))

    # Creat a ShiftSupervisor object
    supervisor = ShiftSupervisor(name, number, annual_salary, annual_bonus)

    # Display ShiftSupervisor information
    print("\nShift Supervisor Information:")
    print(f"Name: {supervisor.get_name()}")
    print(f"Number: {supervisor.get_number()}")
    print(f"Annual Salary: ${supervisor.get_annual_salary():,.2f}")
    print(f"Annual Production Bonus: ${supervisor.get_annual_bonus():,.2f}")
    print(
        f"Total Annual Salary: ${supervisor.get_annual_salary()+supervisor.get_annual_bonus():,.2f}"
    )


if __name__ == "__main__":
    main()
