# Initialize employee data dictionary
employees = {
    101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000},
    102: {'name': 'Anita', 'age': 30, 'department': 'Finance', 'salary': 60000},
    103: {'name': 'Ravi', 'age': 25, 'department': 'IT', 'salary': 55000},
    104: {'name': 'Meena', 'age': 28, 'department': 'Marketing', 'salary': 52000},
    105: {'name': 'Abhinav', 'age': 29, 'department': 'AI', 'salary': 70000}
}

print(employees)

"""# Defining the Menu System for EMS"""

def display_menu():
    print("\n===== Employee Management System =====")
    print("1. Add Employee")
    print("2. View All Employees")
    print("3. Search for Employee")
    print("4. Exit")

# Main loop
while True:
    display_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
      print("Add Employee.")
      while True:
        try:
            emp_id = int(input("Enter Employee ID: "))
        except ValueError:
            print("Invalid input. Employee ID must be a number.")
            continue
        if emp_id in employees:
            print("Employee ID already exists. Please enter a unique ID.")
        else:
            break

      name = input("Enter Employee Name: ")
      while True:
        try:
            age = int(input("Enter Employee Age: "))
            break
        except ValueError:
            print("Invalid input. Age must be a number.")

      department = input("Enter Employee Department: ")
      while True:
        try:
            salary = float(input("Enter Employee Salary: "))
            break
        except ValueError:
            print("Invalid input. Salary must be a number.")

      # Store employee data
      employees[emp_id] = {
        'name': name,
        'age': age,
        'department': department,
        'salary': salary
    }

      print(f"Employee {name} (ID: {emp_id}) successfully added!")

    elif choice == "2":
      print("View All Employees.")
      if not employees:
        print("No employees available.")
      else:
        print("\nEmployee List:")
        for emp_id, details in employees.items():
            print(f"ID: {emp_id}, Name: {details['name']}, Age: {details['age']}, "
                  f"Department: {details['department']}, Salary: {details['salary']}")

    elif choice == "3":
        print("Search for Employee.")
        emp_id = int(input("Enter Employee ID to search: "))
        if emp_id in employees:
          details = employees[emp_id]
          print(f"Found Employee - ID: {emp_id}, Name: {details['name']}, Age: {details['age']}, "
              f"Department: {details['department']}, Salary: {details['salary']}")
        else:
          print("Employee not found.")

    elif choice == "4":
        print("Exit")
        print("Thank You")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")

# End of EMS code