# Class for storing employee details & attributes
class Employee:
    def __init__(self, firstn, lastn, role, pay):
        self.firstn = firstn  # Initialize first name
        self.lastn = lastn    # Initialize last name
        self.role = role      # Initialize role
        self.pay = pay        # Initialize pay

    def fullname(self):
        # Return full name by combining first and last name
        return '{} {}'.format(self.firstn, self.lastn)


# Dictionary to store employee objects
employees = {}


def create_employee(emp_id):
    print("\nAdding a new employee. Please provide the following details:")

    # Prompt the user for employee details
    firstn = input("\nPlease enter the first name: ")
    lastn = input("\nPlease enter the last name: ")
    role = input("\nPlease enter the desired role: ")

    # Loop to ensure valid pay input
    while True:
        try:
            pay = int(input("\nPlease enter the pay expectations as a whole number: "))
            break  # Exit loop if valid number is entered
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    # Create a new Employee object with the provided details
    new_emp = Employee(firstn, lastn, role, pay)

    # Add the new employee to the dictionary with the generated emp_id
    employees[emp_id] = new_emp

    print(f"\nEmployee {new_emp.fullname()} has been added to the list.")


def display_employees():
    # Check if there are no employees
    if not employees:
        print("\nNo employees have been added yet.")
    else:
        print("\nList of employees:")
        # Iterate over the employees dictionary and print details
        for emp_id, emp in employees.items():
            print(f"{emp_id}: Name: {emp.fullname()}, Role: {emp.role}, Pay: ${emp.pay}")


def remove_employee():
    # Check if there are no employees to remove
    if not employees:
        print("\nNo employees to remove.")
        return

    # Prompt the user for the employee ID to remove
    emp_id = input("\nEnter the employee ID to remove (e.g., emp_1): ")
    if emp_id in employees:
        emp = employees[emp_id]  # Retrieve the employee object
        del employees[emp_id]    # Remove the employee from the dictionary
        print(f"\n({emp_id}): {emp.fullname()} has been removed.")
    else:
        print("\nEmployee ID not found.")


def duplicate_employee(emp_id):
    # Check if there are no employees to duplicate
    if not employees:
        print("\nNo employees to duplicate.")
        return False

    # Prompt the user for the employee ID to duplicate
    orig_emp_id = input("\nEnter the employee ID to duplicate (e.g., emp_1): ")
    if orig_emp_id in employees:
        orig_emp = employees[orig_emp_id]  # Retrieve the original employee object

        # Prompt the user for the new first and last names
        firstn = input("\nPlease enter the new first name: ")
        lastn = input("\nPlease enter the new last name: ")

        # Create a new Employee object with the new names but same role and pay
        new_emp = Employee(firstn, lastn, orig_emp.role, orig_emp.pay)

        # Add the new employee to the dictionary with the new emp_id
        employees[emp_id] = new_emp

        print(f"\nEmployee {new_emp.fullname()} has been added to the list with the same role and pay as {orig_emp.fullname()}.")
        return True
    else:
        print("\nOriginal employee ID not found.")
        return False


def main_menu():
    emp_counter = 1  # Initialize employee counter

    while True:
        # Display the main menu options
        print("\nMain Menu:")
        print("1. Add a new employee")
        print("2. Display all employees")
        print("3. Remove an employee")
        print("4. Duplicate an employee")
        print("5. Exit")

        # Get user's choice
        choice = input("\nEnter your choice: ")

        # Perform actions based on user's choice
        if choice == '1':
            emp_id = f"emp_{emp_counter}"  # Generate employee ID
            create_employee(emp_id)        # Call function to create employee
            emp_counter += 1               # Increment employee counter
        elif choice == '2':
            display_employees()            # Call function to display employees
        elif choice == '3':
            remove_employee()              # Call function to remove employee
        elif choice == '4':
            emp_id = f"emp_{emp_counter}"  # Generate employee ID for new duplicate
            if duplicate_employee(emp_id): # Call function to duplicate employee
                emp_counter += 1           # Increment employee counter only if duplication is successful
        elif choice == '5':
            print("Exiting the program.")
            break                          # Exit the loop to end the program
        else:
            print("Invalid choice. Please select a valid option.")


# Start the main menu
try:
    main_menu()  # Call the main menu function to start the program
except KeyboardInterrupt:
    print("\nProgram interrupted. Exiting The Company. Have a great day!")
    exit()  # Exit the program gracefully on keyboard interrupt
