from tkinter import *
from tkinter import messagebox

# -----------------------------
# Functions
# -----------------------------

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()

        for task in tasks:
            task_listbox.insert(END, task.strip())

    except FileNotFoundError:
        pass


def save_tasks():
    tasks = task_listbox.get(0, END)

    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")


def add_task():
    task = task_entry.get().strip()

    if task != "":
        task_listbox.insert(END, task)
        task_entry.delete(0, END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Please enter a task.")


def delete_task():
    try:
        selected = task_listbox.curselection()[0]
        task_listbox.delete(selected)
        save_tasks()
    except:
        messagebox.showwarning("Warning", "Please select a task.")


def mark_completed():
    try:
        selected = task_listbox.curselection()[0]
        task = task_listbox.get(selected)

        if not task.startswith("✔ "):
            task_listbox.delete(selected)
            task_listbox.insert(selected, "✔ " + task)

        save_tasks()

    except:
        messagebox.showwarning("Warning", "Please select a task.")


# -----------------------------
# GUI Window
# -----------------------------

root = Tk()
root.title("To-Do List")
root.geometry("500x550")
root.configure(bg="#E8F0FE")

title = Label(
    root,
    text="TO-DO LIST",
    font=("Arial", 20, "bold"),
    bg="#E8F0FE",
    fg="blue"
)

title.pack(pady=15)

# -----------------------------
# Entry Box
# -----------------------------

task_entry = Entry(
    root,
    font=("Arial", 14),
    width=30
)

task_entry.pack(pady=10)

# -----------------------------
# Buttons
# -----------------------------

add_button = Button(
    root,
    text="Add Task",
    width=15,
    bg="green",
    fg="white",
    command=add_task
)

add_button.pack(pady=5)

complete_button = Button(
    root,
    text="Mark Completed",
    width=15,
    bg="blue",
    fg="white",
    command=mark_completed
)

complete_button.pack(pady=5)

delete_button = Button(
    root,
    text="Delete Task",
    width=15,
    bg="red",
    fg="white",
    command=delete_task
)

delete_button.pack(pady=5)

# -----------------------------
# Listbox
# -----------------------------

task_listbox = Listbox(
    root,
    width=45,
    height=15,
    font=("Arial", 13),
    selectbackground="skyblue"
)

task_listbox.pack(pady=15)

# -----------------------------
# Load Saved Tasks
# -----------------------------

load_tasks()

# -----------------------------
# Run Program
# -----------------------------

root.mainloop()