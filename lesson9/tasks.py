
import json
import csv

def load_tasks(filename="tasks.json"):
    try:
        with open(filename, "r") as file:
            tasks = json.load(file)
        return tasks
    except FileNotFoundError:
        print("Error: tasks.json file not found.")
        return []

def display_tasks(tasks):
    print("\n--- Task List ---")
    print(f"{'ID':<5}{'Task Name':<25}{'Completed':<15}{'Priority':<10}")
    print("-" * 55)

    for task in tasks:
        print(
            f"{task['id']:<5}"
            f"{task['task']:<25}"
            f"{str(task['completed']):<15}"
            f"{task['priority']:<10}"
        )


def save_tasks(tasks, filename="tasks.json"):
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4)
    print("\nTasks saved successfully!")

def calculate_stats(tasks):
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task["completed"])
    pending_tasks = total_tasks - completed_tasks

    if total_tasks > 0:
        average_priority = sum(
            task["priority"] for task in tasks
        ) / total_tasks
    else:
        average_priority = 0

    print("\n--- Task Statistics ---")
    print("Total tasks:", total_tasks)
    print("Completed tasks:", completed_tasks)
    print("Pending tasks:", pending_tasks)
    print(f"Average priority: {average_priority:.2f}")

def convert_to_csv(tasks, filename="tasks.csv"):
    with open(filename, "w", newline="") as file:
        fieldnames = ["ID", "Task", "Completed", "Priority"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        for task in tasks:
            writer.writerow({
                "ID": task["id"],
                "Task": task["task"],
                "Completed": task["completed"],
                "Priority": task["priority"]
            })

    print(f"\nTasks exported to {filename} successfully!")

def main():
    tasks = load_tasks()

    if not tasks:
        print("No tasks available.")
        return

    display_tasks(tasks)
    calculate_stats(tasks)

    
    convert_to_csv(tasks)


if __name__ == "__main__":
    main()
