import json

TASK_FILE = "tasks.json"

def load_tasks():
    """Load tasks from a file."""
    try:
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    """Save tasks to a file."""
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def show_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("\nNo tasks in your to-do list.")
        return
    print("\nYour To-Do List:")
    for i, task in enumerate(tasks, 1):
        status = "✔" if task["completed"] else "✘"
        print(f"{i}. {task['description']} [{status}]")

def add_task(tasks):
    """Add a new task."""
    description = input("Enter the task description: ").strip()
    if description:
        tasks.append({"description": description, "completed": False})
        print("Task added successfully!")
    else:
        print("Task description cannot be empty.")

def mark_task_completed(tasks):
    """Mark a task as completed."""
    show_tasks(tasks)
    try:
        task_no = int(input("Enter the task number to mark as completed: "))
        if 1 <= task_no <= len(tasks):
            tasks[task_no - 1]["completed"] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    """Delete a task."""
    show_tasks(tasks)
    try:
        task_no = int(input("Enter the task number to delete: "))
        if 1 <= task_no <= len(tasks):
            tasks.pop(task_no - 1)
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def to_do_list():
    """Main function to manage the to-do list."""
    tasks = load_tasks()

    while True:
        print("\n--- To-Do List Menu ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_task_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Your tasks have been saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    to_do_list()
