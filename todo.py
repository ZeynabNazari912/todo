# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 11:44:18 2024

@author: UOD Student
"""

import json

def load_tasks(filename="tasks.json"):
    """Load tasks from a file."""
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks, filename="tasks.json"):
    """Save tasks to a file."""
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    """Add a new task to the list."""
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    deadline = input("Enter task deadline (YYYY-MM-DD): ")
    tasks.append({"title": title, "description": description, "deadline": deadline})
    print("Task added successfully!")

def update_task(tasks):
    """Update an existing task."""
    view_tasks(tasks)
    try:
        task_index = int(input("Enter the task number to update: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks[task_index]["title"] = input(f"New title ({tasks[task_index]['title']}): ") or tasks[task_index]['title']
            tasks[task_index]["description"] = input(f"New description ({tasks[task_index]['description']}): ") or tasks[task_index]['description']
            tasks[task_index]["deadline"] = input(f"New deadline ({tasks[task_index]['deadline']}): ") or tasks[task_index]['deadline']
            print("Task updated successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_task(tasks):
    """Delete a task from the list."""
    view_tasks(tasks)
    try:
        task_index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks.pop(task_index)
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def view_tasks(tasks):
    """View all tasks."""
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task['title']} (Deadline: {task['deadline']})")
            print(f"   Description: {task['description']}")

def main():
    """Main function to run the to-do list application."""
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Application")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "3":
            update_task(tasks)
            save_tasks(tasks)
        elif choice == "4":
            delete_task(tasks)
            save_tasks(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
