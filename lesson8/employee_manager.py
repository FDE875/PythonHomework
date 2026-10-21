class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return (
            f"ID: {self.employee_id}, "
            f"Name: {self.name}, "
            f"Position: {self.position}, "
            f"Salary: {self.salary:g}"
        )

    def to_file(self):
        return (
            f"{self.employee_id}|{self.name}|"
            f"{self.position}|{self.salary:g}\n"
        )


class EmployeeManager:
    def __init__(self, filename="employees.txt"):
        self.filename = filename

        
        with open(self.filename, "a", encoding="utf-8"):
            pass

    def load_employees(self):
        employees = []

        with open(self.filename, "r", encoding="utf-8") as file:
            for line in file:
                data = line.strip().split("|")

                if len(data) == 4:
                    employee = Employee(
                        data[0],
                        data[1],
                        data[2],
                        float(data[3])
                    )
                    employees.append(employee)

        return employees

    def save_employees(self, employees):
        with open(self.filename, "w", encoding="utf-8") as file:
            for employee in employees:
                file.write(employee.to_file())

    def add_employee(self):
        employees = self.load_employees()

        employee_id = input("Employee ID: ").strip()

        if any(e.employee_id == employee_id for e in employees):
            print("Bu ID allaqachon mavjud!")
            return

        name = input("Name: ").strip()
        position = input("Position: ").strip()

        try:
            salary = float(input("Salary: "))
            if salary < 0:
                print("Maosh manfiy bo'lishi mumkin emas!")
                return
        except ValueError:
            print("Maoshni son bilan kiriting!")
            return

        employee = Employee(employee_id, name, position, salary)

        with open(self.filename, "a", encoding="utf-8") as file:
            file.write(employee.to_file())

        print("Xodim muvaffaqiyatli qo'shildi!")

    def view_employees(self):
        employees = self.load_employees()

        if not employees:
            print("Hozircha xodimlar mavjud emas.")
            return

        for employee in employees:
            print(employee)

    def search_employee(self):
        employee_id = input("Qidirilayotgan Employee ID: ").strip()

        for employee in self.load_employees():
            if employee.employee_id == employee_id:
                print(employee)
                return

        print("Xodim topilmadi!")

    def update_employee(self):
        employees = self.load_employees()
        employee_id = input("Yangilanadigan Employee ID: ").strip()

        for employee in employees:
            if employee.employee_id == employee_id:
                print("Joriy ma'lumotlar:")
                print(employee)
                print("O'zgartirmaslik uchun maydonni bo'sh qoldiring.")

                name = input(f"Yangi ism [{employee.name}]: ").strip()
                position = input(
                    f"Yangi lavozim [{employee.position}]: "
                ).strip()
                salary_text = input(
                    f"Yangi maosh [{employee.salary:g}]: "
                ).strip()

                if name:
                    employee.name = name

                if position:
                    employee.position = position

                if salary_text:
                    try:
                        salary = float(salary_text)
                        if salary < 0:
                            print("Maosh manfiy bo'lishi mumkin emas!")
                            return
                        employee.salary = salary
                    except ValueError:
                        print("Maoshni son bilan kiriting!")
                        return

                self.save_employees(employees)
                print("Ma'lumotlar yangilandi!")
                return

        print("Xodim topilmadi!")

    def delete_employee(self):
        employees = self.load_employees()
        employee_id = input("O'chiriladigan Employee ID: ").strip()

        for employee in employees:
            if employee.employee_id == employee_id:
                employees.remove(employee)
                self.save_employees(employees)
                print("Xodim o'chirildi!")
                return

        print("Xodim topilmadi!")


def main():
    manager = EmployeeManager()

    while True:
        print("\n===== EMPLOYEE RECORDS MANAGER =====")
        print("1. Add new employee record")
        print("2. View all employee records")
        print("3. Search for an employee by Employee ID")
        print("4. Update an employee's information")
        print("5. Delete an employee record")
        print("6. Exit")

        choice = input("Tanlovingiz (1-6): ").strip()

        if choice == "1":
            manager.add_employee()
        elif choice == "2":
            manager.view_employees()
        elif choice == "3":
            manager.search_employee()
        elif choice == "4":
            manager.update_employee()
        elif choice == "5":
            manager.delete_employee()
        elif choice == "6":
            print("Dastur yakunlandi!")
            break
        else:
            print("Noto'g'ri tanlov! 1 dan 6 gacha kiriting.")


if __name__ == "__main__":
    main()