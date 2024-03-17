# Initialize an empty list to store the tasks
tasks = []

def display_menu():
    """Display the menu of options"""
    print("\nTo-Do List")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. View tasks")
    print("4. Exit")

def add_task():
    """Add a new task to the list"""
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added successfully!")

def remove_task():
    """Remove a task from the list"""
    if not tasks:
        print("No tasks to remove.")
    else:
        print("Current tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
        choice = int(input("Enter the number of the task to remove: "))
        if 1 <= choice <= len(tasks):
            removed_task = tasks.pop(choice - 1)
            print(f"Removed task: {removed_task}")
        else:
            print("Invalid choice.")

def view_tasks():
    """View all tasks in the list"""
    if not tasks:
        print("No tasks to view.")
    else:
        print("Current tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            add_task()
        elif choice == "2":
            remove_task()
        elif choice == "3":
            view_tasks()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()