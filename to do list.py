
import random
import string
# ================================
# TO-DO LIST APPLICATION
# ================================
# This program allows the user to:
# 1. Add tasks
# 2. View tasks
# 3. Update tasks
# 4. Remove tasks
# 5. Exit the program

# We will use a Python list to store tasks.

tasks = []  # Empty list to store all tasks

def show_menu():
    """Display the menu options to the user"""
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Remove Task")
    print("5. Exit")

while True:
    show_menu()  # Show menu every time
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        # Add a new task
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        # View all tasks
        if not tasks:
            print("No tasks found!")
        else:
            print("\nYour Tasks:")
            for i, t in enumerate(tasks, 1):
                print(i, "-", t)

    elif choice == "3":
        # Update an existing task
        if not tasks:
            print("No tasks to update!")
        else:
            num = int(input("Enter task number to update: "))
            if 0 < num <= len(tasks):
                new_task = input("Enter updated task: ")
                tasks[num-1] = new_task
                print("Task updated successfully!")
            else:
                print("Invalid task number!")

    elif choice == "4":
        # Remove a task
        if not tasks:
            print("No tasks to remove!")
        else:
            num = int(input("Enter task number to remove: "))
            if 0 < num <= len(tasks):
                removed = tasks.pop(num-1)
                print("Removed:", removed)
            else:
                print("Invalid task number!")

    elif choice == "5":
        # Exit the program
        print("Goodbye! Exiting To-Do List...")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 5.")