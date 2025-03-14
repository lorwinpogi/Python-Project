todo_list = []  # List to store tasks

def show_tasks():
    """Displays all tasks in the to-do list."""
    if not todo_list:
        print("\nNo tasks in the list.")
    else:
        print("\nTo-Do List:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

def add_task():
    """Adds a task to the to-do list."""
    task = input("\nEnter a task: ")
    todo_list.append(task)
    print(f"Task '{task}' added successfully!")

def remove_task():
    """Removes a task from the to-do list."""
    show_tasks()
    if todo_list:
        try:
            task_num = int(input("\nEnter task number to remove: "))
            removed_task = todo_list.pop(task_num - 1)
            print(f"Task '{removed_task}' removed successfully!")
        except (ValueError, IndexError):
            print("Invalid task number!")

def main():
    """Main function to run the to-do list program."""
    while True:
        print("\nTo-Do List Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("\nExiting the To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")

# Run the To-Do List program
if __name__ == "__main__":
    main()
