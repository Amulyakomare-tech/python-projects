import os
import json

TASKS_FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task(tasks):
    task = input("Enter task description: ")
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)
    print("Task added successfully!\n")

# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.\n")
        return
    print("\n--- TO-DO LIST ---")
    for i, t in enumerate(tasks, start=1):
        status = "✓ Completed" if t["completed"] else "✗ Not Completed"
        print(f"{i}. {t['task']} - {status}")
    print()

# Mark a task as completed
def mark_completed(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        index = int(input("Enter task number to mark as completed: ")) - 1
        tasks[index]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed!\n")
    except:
        print("Invalid selection!\n")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        index = int(input("Enter task number to delete: ")) - 1
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"Deleted task: {removed['task']}\n")
    except:
        print("Invalid task number!\n")

# Main Program Loop
def main():
    tasks = load_tasks()

    while True:
        print("=== TO-DO LIST MENU ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Try again.\n")

if __name__ == "__main__":
    main()
