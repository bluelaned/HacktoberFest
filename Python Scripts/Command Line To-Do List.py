tasks = []

def display_menu():
    print("\nTo-Do List:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    print("\nOptions:")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. Exit")

def add_task():
    task = input("Enter the task: ")
    tasks.append(task)

def remove_task():
    display_menu()
    task_num = int(input("Enter the task number to remove: "))
    if 0 < task_num <= len(tasks):
        tasks.pop(task_num - 1)
    else:
        print("Invalid task number")

if __name__ == "__main__":
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            add_task()
        elif choice == '2':
            remove_task()
        elif choice == '3':
            break
        else:
            print("Invalid choice, try again.")
