# File: todo.py

# Function to add tasks
def add_task(filename, task):
    with open(filename, 'a') as file:  # 'a' = append mode
        file.write(task + '\n')
    print(f"Task added: {task}")

# Function to show all tasks
def show_tasks(filename):
    print("\nYour To-Do List:")
    try:
        with open(filename, 'r') as file:
            tasks = file.readlines()
            if not tasks:
                print("No tasks found.")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("Task file not found.")

# Main Menu
def menu():
    filename = 'tasks.txt'
    while True:
        print("\n--- To-Do List ---")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter your task: ")
            add_task(filename, task)
        elif choice == '2':
            show_tasks(filename)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# Run the program
menu()
