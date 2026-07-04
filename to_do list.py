"""
To-Do List - Project 1 (Upgraded Version)
Builds on the basic list+append+print version by adding:
- Dictionaries instead of plain strings (task records with id/task/done)
- enumerate() for clean display
- JSON file persistence (so tasks survive after closing the program)
- Mark as done / Delete (basic CRUD)
"""

import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    """Load tasks from disk. Returns an empty list if no file exists yet."""
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    """Persist the current task list to disk as JSON."""
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=2)


def add_task(tasks, description):
    new_id = (tasks[-1]["id"] + 1) if tasks else 1
    tasks.append({"id": new_id, "task": description, "done": False})
    save_tasks(tasks)
    print(f"Added: '{description}'")


def view_tasks(tasks):
    if not tasks:
        print("No tasks yet. Add one!")
        return
    print("\n--- YOUR TASKS ---")
    for index, t in enumerate(tasks):
        status = "✔" if t["done"] else "✗"
        print(f"{index + 1}. [{status}] {t['task']} (id: {t['id']})")
    print("------------------\n")


def mark_done(tasks, task_id):
    for t in tasks:
        if t["id"] == task_id:
            t["done"] = True
            save_tasks(tasks)
            print(f"Marked task {task_id} as done.")
            return
    print("Task ID not found.")


def delete_task(tasks, task_id):
    new_tasks = [t for t in tasks if t["id"] != task_id]
    if len(new_tasks) == len(tasks):
        print("Task ID not found.")
    else:
        save_tasks(new_tasks)
        print(f"Deleted task {task_id}.")
    return new_tasks


def main():
    tasks = load_tasks()

    menu = """
1. Add task
2. View tasks
3. Mark task as done
4. Delete task
5. Exit
"""
    while True:
        print(menu)
        choice = input("Choose an option: ").strip()

        if choice == "1":
            description = input("Enter task: ").strip()
            if description:
                add_task(tasks, description)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            view_tasks(tasks)
            try:
                task_id = int(input("Enter task id to mark done: "))
                mark_done(tasks, task_id)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            view_tasks(tasks)
            try:
                task_id = int(input("Enter task id to delete: "))
                tasks = delete_task(tasks, task_id)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "5":
            print("Goodbye! Your tasks are saved in tasks.json")
            break

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
