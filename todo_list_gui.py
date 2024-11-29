import tkinter as tk
from tkinter import messagebox
import json

TASK_FILE = "tasks_gui.json"

def load_tasks():
    try:
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def update_task_list():
    listbox.delete(0, tk.END)
    for task in tasks:
        status = "✔" if task["completed"] else "✘"
        listbox.insert(tk.END, f"{task['description']} [{status}]")

def add_task():
    task_description = task_entry.get().strip()
    if task_description:
        tasks.append({"description": task_description, "completed": False})
        update_task_list()
        save_tasks(tasks)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task description cannot be empty.")

def mark_task_completed():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        tasks[index]["completed"] = True
        update_task_list()
        save_tasks(tasks)
    else:
        messagebox.showwarning("Warning", "Please select a task to mark as completed.")

def delete_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        del tasks[index]
        update_task_list()
        save_tasks(tasks)
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Initialize the GUI
root = tk.Tk()
root.title("To-Do List")

tasks = load_tasks()

# Task Entry
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

# Buttons
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

complete_button = tk.Button(root, text="Mark Completed", command=mark_task_completed)
complete_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

# Task List
listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

update_task_list()

# Start the GUI event loop
root.mainloop()
