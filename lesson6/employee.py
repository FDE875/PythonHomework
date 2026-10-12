FILE_NAME = "employees.txt"

def add_employee():
    employee_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    position = input("Enter Position: ")
    salary = input("Enter Salary: ")

    with open(FILE_NAME, "a", encoding="utf-8") as file:
        file.write(f"{employee_id}, {name}, {position}, {salary}\n")

    print("Employee added successfully!")

def view_employees():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            records = file.readlines()

        if not records:
            print("No employee records found.")
        else:
            for record in records:
                print(record.strip())

    except FileNotFoundError:
        print("No employee records found.")

def search_employee():
    employee_id = input("Enter Employee ID to search: ")

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            for record in file:
                data = record.strip().split(", ")

                if len(data) == 4 and data[0] == employee_id:
                    print("Employee found:")
                    print(record.strip())
                    return

        print("Employee not found.")

    except FileNotFoundError:
        print("No employee records found.")

def update_employee():
    employee_id = input("Enter Employee ID to update: ")

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            records = file.readlines()
    except FileNotFoundError:
        print("No employee records found.")
        return

    for i, record in enumerate(records):
        data = record.strip().split(", ")

        if len(data) == 4 and data[0] == employee_id:
            print("1. Update Name")
            print("2. Update Position")
            print("3. Update Salary")

            choice = input("Choose what to update: ")

            if choice == "1":
                data[1] = input("Enter new name: ")
            elif choice == "2":
                data[2] = input("Enter new position: ")
            elif choice == "3":
                data[3] = input("Enter new salary: ")
            else:
                print("Invalid choice.")
                return

            records[i] = ", ".join(data) + "\n"

            with open(FILE_NAME, "w", encoding="utf-8") as file:
                file.writelines(records)

            print("Employee updated successfully!")
            return

    print("Employee not found.")

def delete_employee():
    employee_id = input("Enter Employee ID to delete: ")

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            records = file.readlines()
    except FileNotFoundError:
        print("No employee records found.")
        return

    updated_records = []
    found = False

    for record in records:
        data = record.strip().split(", ")

        if len(data) == 4 and data[0] == employee_id:
            found = True
        else:
            updated_records.append(record)

    if found:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            file.writelines(updated_records)

        print("Employee deleted successfully!")
    else:
        print("Employee not found.")

while True:
    print("\n===== Employee Records Manager =====")
    print("1. Add new employee record")
    print("2. View all employee records")
    print("3. Search for an employee by Employee ID")
    print("4. Update an employee's information")
    print("5. Delete an employee record")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        view_employees()
    elif choice == "3":
        search_employee()
    elif choice == "4":
        update_employee()
    elif choice == "5":
        delete_employee()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 6.")