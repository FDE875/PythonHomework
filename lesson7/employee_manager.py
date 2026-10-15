import os


class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary:g}"

    def to_file(self):
        return f"{self.employee_id}|{self.name}|{self.position}|{self.salary}\n"


class EmployeeManager:
    def __init__(self, filename="employees.txt"):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, "w", encoding="utf-8"):
                pass

    def load_employees(self):
        employees = []
        if not os.path.exists(self.filename):
            return employees

        with open(self.filename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                
                parts = line.split("|")
                if len(parts) != 4:
                    continue  
                
                employee_id, name, position, salary = parts
                try:
                    employee = Employee(employee_id, name, position, float(salary))
                    employees.append(employee)
                except ValueError:
                    continue

        return employees

    def save_employees(self, employees):
        with open(self.filename, "w", encoding="utf-8") as file:
            for employee in employees:
                file.write(employee.to_file())

    def add_employee(self):
        employee_id = input("Enter Employee ID: ").strip()
        employees = self.load_employees()

        if any(e.employee_id == employee_id for e in employees):
            print("Error: Employee ID already exists!")
            return

        name = input("Enter Name: ").strip()
        position = input("Enter Position: ").strip()

        try:
            salary = float(input("Enter Salary: "))
            if salary < 0:
                print("Salary cannot be negative!")
                return
        except ValueError:
            print("Invalid salary! Please enter a number.")
            return

        employee = Employee(employee_id, name, position, salary)

        with open(self.filename, "a", encoding="utf-8") as file:
            file.write(employee.to_file())

        print("Employee added successfully!")

    def view_all_employees(self):
        employees = self.load_employees()
        if not employees:
            print("No employee records found.")
            return

        print("\nEmployee Records:")
        for employee in employees:
            print(employee)

    def search_employee(self):
        employee_id = input("Enter Employee ID to search: ").strip()
        for employee in self.load_employees():
            if employee.employee_id == employee_id:
                print("\nEmployee Found:")
                print(employee)
                return

        print("Employee not found!")

    def update_employee(self):
        employee_id = input("Enter Employee ID to update: ").strip()
        employees = self.load_employees()

        for employee in employees:
            if employee.employee_id == employee_id:
                print("Leave a field empty to keep its current value.")

                name = input(f"Enter Name [{employee.name}]: ").strip()
                position = input(f"Enter Position [{employee.position}]: ").strip()
                salary_input = input(f"Enter Salary [{employee.salary:g}]: ").strip()

                if name:
                    employee.name = name
                if position:
                    employee.position = position

                if salary_input:
                    try:
                        salary = float(salary_input)
                        if salary < 0:
                            print("Salary cannot be negative!")
                            return
                        employee.salary = salary
                    except ValueError:
                        print("Invalid salary! Update cancelled.")
                        return

                self.save_employees(employees)
                print("Employee updated successfully!")
                return

        print("Employee not found!")

    def delete_employee(self):
        employee_id = input("Enter Employee ID to delete: ").strip()
        employees = self.load_employees()

        for employee in employees:
            if employee.employee_id == employee_id:
                employees.remove(employee)
                self.save_employees(employees)
                print("Employee deleted successfully!")
                return

        print("Employee not found!")

    def menu(self):
        while True:
            print("\nWelcome to the Employee Records Manager!")
            print("1. Add new employee record")
            print("2. View all employee records")
            print("3. Search for an employee by Employee ID")
            print("4. Update an employee's information")
            print("5. Delete an employee record")
            print("6. Exit")

            choice = input("\nEnter your choice: ").strip()

            if choice == "1":
                self.add_employee()
            elif choice == "2":
                self.view_all_employees()
            elif choice == "3":
                self.search_employee()
            elif choice == "4":
                self.update_employee()
            elif choice == "5":
                self.delete_employee()
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice! Please choose 1-6.")


if __name__ == "__main__":
    manager = EmployeeManager()
    manager.menu()
    