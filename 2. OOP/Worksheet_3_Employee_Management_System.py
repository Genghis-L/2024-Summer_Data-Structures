# Copyright 2024 Genghis, 骆可瀚(Luo Kehan), kl4747@nyu.edu

# Basic funcionalities, optimization needed.

import pickle


class Employee:
    """Employee Class"""

    def __init__(self, name, ID, department, job) -> None:
        self.name = name
        self.__ID = ID
        self.department = department
        self.job = job

    def __str__(self) -> str:
        return f"{self.__ID}: ({self.name}, {self.department}, {self.job})"


def load_employees(filename):
    """load pickle"""

    try:
        with open(filename, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return {}


def save_employees(filename, employees):
    """save pickle"""

    with open(filename, "wb") as file:
        pickle.dump(employees, file)


def display_menu():
    """display Menu"""

    print("\nEmployee Management System")
    print("1. Look up an employee")
    print("2. Add a new employee")
    print("3. Change an existing employee's name, department, and job title")
    print("4. Delete an employee")
    print("5. Quit the program")


def look_up_employee(employees):
    """looking up"""

    id = input("Please input the employee's ID: ")
    try:
        print(employees[id])
    except KeyError:
        print("Employee Not Found. ")


def add_employee(employees):
    """adding"""

    name = input("Please enter the employee's name: ")
    id = input("Please enter the employee's ID: ")
    department = input("Please enter the employee's department: ")
    job = input("Please enter the employee's job: ")

    if id in employees.keys():
        print("The employee has already existed. ")
    else:
        employees[id] = Employee(name, id, department, job)
        print("The employee has been added successfully. ")


def change_employee(employees):
    """changing"""

    id = input("Please input the employee's ID: ")
    if id not in employees:
        print("Employee Not Found. ")
    else:
        new_name = input("Enter new name: ")
        new_department = input("Enter new department: ")
        new_job = input("Enter new job: ")
        employees[id].name = new_name
        employees[id].department = new_department
        employees[id].job = new_job
        print("Employee information has been updated successfully. ")


def delete_employee(employees):
    """deleting"""

    id = input("Please input the employee's ID: ")
    if id not in employees:
        print("Employee Not Found. ")
    else:
        del employees[id]
        print("The employee has been deleted successfully. ")


def main():
    filename = "employees.pkl"

    employees = load_employees(filename)

    if employees == {}:
        employees["47899"] = Employee(
            "Susan Meyers", "47899", "Accounting", "Vice President"
        )
        employees["39119"] = Employee("Mark Jones", "39119", "IT", "Programmer")
        employees["81774"] = Employee(
            "Joy Rogers", "81774", "Manufacturing", "Engineer"
        )

    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            look_up_employee(employees)
        elif choice == "2":
            add_employee(employees)
        elif choice == "3":
            change_employee(employees)
        elif choice == "4":
            delete_employee(employees)
        elif choice == "5":
            save_employees(filename, employees)
            print("Employees data saved. Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
