from abc import ABC, abstractmethod
import csv
import json
import os


class Task:
    """Vazifa (Task) obyektini tavsiflovchi sinf."""

    def __init__(self, task_id, title, description, due_date="", status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def __str__(self):
        return f"{self.task_id}, {self.title}, {self.description}, {self.due_date}, {self.status}"

    def to_dict(self):
        """JSON va boshqa formatlar uchun lug'atga o'girish."""
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status,
        }

    @classmethod
    def from_dict(cls, data):
        """Lug'atdan Task obyektini yaratish."""
        return cls(
            task_id=data.get("task_id"),
            title=data.get("title"),
            description=data.get("description"),
            due_date=data.get("due_date", ""),
            status=data.get("status", "Pending"),
        )


class StorageStrategy(ABC):
    """Saqlash strategiyalari uchun mavhum (abstract) sinf."""

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def save(self, tasks):
        pass


class CsvStorage(StorageStrategy):
    """CSV formatida saqlash va yuklash."""

    def __init__(self, filename="tasks.csv"):
        self.filename = filename

    def load(self):
        tasks = []
        if not os.path.exists(self.filename):
            return tasks

        with open(self.filename, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                tasks.append(Task.from_dict(row))
        return tasks

    def save(self, tasks):
        with open(self.filename, mode="w", newline="", encoding="utf-8") as file:
            fieldnames = ["task_id", "title", "description", "due_date", "status"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for task in tasks:
                writer.writerow(task.to_dict())


class JsonStorage(StorageStrategy):
    """JSON formatida saqlash va yuklash."""

    def __init__(self, filename="tasks.json"):
        self.filename = filename

    def load(self):
        tasks = []
        if not os.path.exists(self.filename):
            return tasks

        with open(self.filename, mode="r", encoding="utf-8") as file:
            try:
                data = json.load(file)
                for item in data:
                    tasks.append(Task.from_dict(item))
            except json.JSONDecodeError:
                pass
        return tasks

    def save(self, tasks):
        with open(self.filename, mode="w", encoding="utf-8") as file:
            data = [task.to_dict() for task in tasks]
            json.dump(data, file, indent=4, ensure_ascii=False)


class TaskManager:
    """Vazifalarni boshqarish va ular ustidan amallarni bajarish sinfi."""

    def __init__(self, storage: StorageStrategy):
        self.storage = storage
        self.tasks = self.storage.load()

    def add_task(self, task: Task):
        if any(t.task_id == task.task_id for t in self.tasks):
            print("Error: Task ID already exists!")
            return False
        self.tasks.append(task)
        print("Task added successfully!")
        return True

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        print("\nTasks:")
        for task in self.tasks:
            print(task)

    def update_task(self, task_id, **kwargs):
        for task in self.tasks:
            if task.task_id == task_id:
                if "title" in kwargs and kwargs["title"]:
                    task.title = kwargs["title"]
                if "description" in kwargs and kwargs["description"]:
                    task.description = kwargs["description"]
                if "due_date" in kwargs:
                    task.due_date = kwargs["due_date"]
                if "status" in kwargs and kwargs["status"]:
                    task.status = kwargs["status"]
                print("Task updated successfully!")
                return True
        print("Task not found!")
        return False

    def delete_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                print("Task deleted successfully!")
                return True
        print("Task not found!")
        return False

    def filter_tasks(self, status):
        filtered = [t for t in self.tasks if t.status.lower() == status.lower()]
        if not filtered:
            print(f"No tasks found with status: {status}")
            return
        print(f"\nTasks with status '{status}':")
        for task in filtered:
            print(task)

    def save_tasks(self):
        self.storage.save(self.tasks)
        print("Tasks saved successfully!")

    def load_tasks(self):
        self.tasks = self.storage.load()
        print("Tasks loaded successfully!")


def main():
    storage = CsvStorage("tasks.csv")
    manager = TaskManager(storage)

    while True:
        print("\nWelcome to the To-Do Application!")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Filter tasks by status")
        print("6. Save tasks")
        print("7. Load tasks")
        print("8. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            task_id = input("Enter Task ID: ").strip()
            title = input("Enter Title: ").strip()
            description = input("Enter Description: ").strip()
            due_date = input("Enter Due Date (YYYY-MM-DD): ").strip()
            status = input(
                "Enter Status (Pending/In Progress/Completed): "
            ).strip()
            if not status:
                status = "Pending"

            new_task = Task(task_id, title, description, due_date, status)
            manager.add_task(new_task)

        elif choice == "2":
            manager.view_tasks()

        elif choice == "3":
            task_id = input("Enter Task ID to update: ").strip()
            print("Leave blank to keep current value.")
            title = input("New Title: ").strip()
            description = input("New Description: ").strip()
            due_date = input("New Due Date (YYYY-MM-DD): ").strip()
            status = input("New Status (Pending/In Progress/Completed): ").strip()

            manager.update_task(
                task_id,
                title=title,
                description=description,
                due_date=due_date,
                status=status,
            )

        elif choice == "4":
            task_id = input("Enter Task ID to delete: ").strip()
            manager.delete_task(task_id)

        elif choice == "5":
            status = input("Enter status to filter by (Pending/In Progress/Completed): ").strip()
            manager.filter_tasks(status)

        elif choice == "6":
            manager.save_tasks()

        elif choice == "7":
            manager.load_tasks()

        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please choose between 1-8.")


if __name__ == "__main__":
    main()
    