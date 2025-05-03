import os
TODO_FILE = "todo.txt"
# Load tasks from file
def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as f:
        return [line.strip() for line in f.readlines()]

# Save tasks to file
def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

# Show menu
def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as completed")
    print("4. Remove task")
    print("5. Exit")

# Main loop
def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            if not tasks:
                print("No tasks yet!")
            else:
                print("\nTasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")

        elif choice == "2":
            task = input("Enter new task: ").strip()
            if task:
                tasks.append(task)
                save_tasks(tasks)
                print("Task added.")
            else:
                print("Task cannot be empty.")

        elif choice == "3":
            if not tasks:
                print("No tasks to mark as completed.")
            else:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
                try:
                    idx = int(input("Enter task number to mark completed: ")) - 1
                    if 0 <= idx < len(tasks):
                        tasks[idx] += " ✅"
                        save_tasks(tasks)
                        print("Task marked as completed.")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "4":
            if not tasks:
                print("No tasks to remove.")
            else:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
                try:
                    idx = int(input("Enter task number to remove: ")) - 1
                    if 0 <= idx < len(tasks):
                        removed = tasks.pop(idx)
                        save_tasks(tasks)
                        print(f"Removed: {removed}")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Choose 1-5.")

if __name__ == "__main__":
    main()
