# Copyright 2024 Genghis, 骆可瀚(Luo Kehan), kl4747@nyu.edu

# Basic funcionalities, Admin mode added, further optimizations like GUI are needed. 


import pickle


class Employee:
    """Class representing an employee.

    Attributes:
        name (str): The name of the employee.
        ID (str): The ID of the employee.
        department (str): The department of the employee.
        job (str): The job title of the employee.
    """

    def __init__(self, name: str, ID: str, department: str, job: str):
        """Initialize Employee with name, ID, department, and job."""
        self.name = name
        self.__ID = ID
        self.department = department
        self.job = job

    def __repr__(self) -> str:
        return f"({self.name}, {self.department}, {self.job})"

    def __str__(self) -> str:
        return f"({self.__ID}: {self.name}, {self.department}, {self.job})"


def load_employees(filename) -> dict:
    """Load employee data from a file.

    Args:
        filename (str): The name of the file to load data from.

    Returns:
        dict: A dictionary containing employee data loaded from the file.

    """

    try:
        with open(filename, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return {}


def save_employees(filename, employees: dict):
    """Save employee data to a file.

    Args:
        filename (str): The name of the file to save data to.
        employees (dict): A dictionary containing employee data to be saved.

    """

    with open(filename, "wb") as file:
        pickle.dump(employees, file)


def display_menu(admin_mode: bool):
    """Display the main menu of the Employee Management System.

    Args:
        admin_mode (bool): A boolean indicating whether the program is in admin mode.

    """

    print("\nEmployee Management System")
    print("1. Look up an employee")

    if admin_mode:
        print("2. Add a new employee")
        print("3. Change an existing employee's name, department, and job title")
        print("4. Delete an employee")
        print("5. Check list of employees")
        print("6. Quit the program")
    else:
        print("2. Quit the program")


def print_separator():
    """Printing Separation"""
    print("\n" + "—" * 60 + "\n")


def look_up_employee(employees: dict):
    """Look up an employee by ID.

    Args:
        employees (dict): A dictionary containing employee data.

    """

    id = input("Please input the employee's ID: ")
    try:
        print(employees[id])
    except KeyError:
        print("Employee Not Found. ")


def add_employee(employees: dict):
    """Add a new employee. (Admin Mode)

    Args:
        employees (dict): A dictionary containing employee data.

    """

    name = input("Please enter the employee's name: ")
    id = input("Please enter the employee's ID: ")
    department = input("Please enter the employee's department: ")
    job = input("Please enter the employee's job: ")

    if id in employees.keys():
        print("The employee already exists. ")
    else:
        employees[id] = Employee(name, id, department, job)
        print("The employee has been added successfully. ")


def change_employee(employees: dict):
    """Change an existing employee's information. (Admin Mode)

    Args:
        employees (dict): A dictionary containing employee data.

    """

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


def delete_employee(employees: dict):
    """Delete an existing employee. (Admin Mode)

    Args:
        employees (dict): A dictionary containing employee data.

    """

    id = input("Please input the employee's ID: ")
    if id not in employees:
        print("Employee Not Found. ")
    else:
        del employees[id]
        print("The employee has been deleted successfully. ")


def check_list(employees: dict):
    """Check the list of employees. (Admin Mode)

    Args:
        employees (dict): A dictionary containing employee data.

    """

    print("\nList of Employees:")
    for employee in employees.values():
        print(employee)


def admin_login() -> bool:
    """Authenticate administrator credentials.

    Returns:
        bool: True if administrator login is successful, False otherwise.

    """

    admin_id = "111"
    admin_password = "111"
    attempts = 3
    while attempts > 0:
        print(f"Administrator Login (Attempts left: {attempts})")
        entered_id = input("Enter Administrator ID: ")
        entered_password = input("Enter Administrator Password: ")

        if entered_id == admin_id and entered_password == admin_password:
            print("Administrator Logged In.")
            return True
        else:
            attempts -= 1
            print(f"Invalid Administrator ID or Password.")
            print_separator()

    print("Max attempts reached. Redirecting to regular mode.")
    return False


def main():
    """Main function to run the Employee Management System."""

    filename = "/Users/kehanluo/Documents/GitHub/2024_Summer_Data-Structures/2. OOP/employees.pkl"

    employees = load_employees(filename)

    if employees == {}:
        employees["47899"] = Employee(
            "Susan Meyers", "47899", "Accounting", "Vice President"
        )
        employees["39119"] = Employee("Mark Jones", "39119", "IT", "Programmer")
        employees["81774"] = Employee(
            "Joy Rogers", "81774", "Manufacturing", "Engineer"
        )

    admin_mode = False
    admin_choice = ""
    while admin_choice.lower() != "no":
        admin_response = input("Are you an administrator? (yes/no): ")
        if admin_response.lower() == "yes":
            admin_mode = admin_login()
            break
        elif admin_response.lower() == "no":
            break
        else:
            print("Invalid response. Please enter 'yes' or 'no'.")

    while True:
        display_menu(admin_mode)
        choice = input("Enter your choice: ")

        if choice == "1":
            look_up_employee(employees)
            print_separator()

        # Regular Mode
        elif choice == "2" and not admin_mode:
            save_employees(filename, employees)
            print("Employees data saved. Exiting the program.")
            print_separator()
            break

        # Admin Mode
        elif choice == "2" and admin_mode:
            add_employee(employees)
            print_separator()
        elif choice == "3" and admin_mode:
            change_employee(employees)
            print_separator()
        elif choice == "4" and admin_mode:
            delete_employee(employees)
            print_separator()
        elif choice == "5" and admin_mode:
            check_list(employees)
            print_separator()
        elif choice == "6" and admin_mode:
            save_employees(filename, employees)
            print("Employees data saved. Exiting the program.")
            print_separator()
            break
        else:
            print("Invalid choice. Please try again.")
            print_separator()


if __name__ == "__main__":
    main()
