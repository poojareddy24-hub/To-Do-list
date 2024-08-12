tasks = []
def show_tasks():
    if tasks:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task['name']} - {'Done' if task['done'] else 'Not Done'}")
    else:
        print("No tasks available.")
def add_task(name):
    tasks.append({"name": name, "done": False})
    print(f"Task '{name}' added.")
def complete_task(num):
    if 0 < num <= len(tasks):
        tasks[num - 1]["done"] = True
        print(f"Task {num} completed.")
    else:
        print("Invalid task number.")
def delete_task(num):
    if 0 < num <= len(tasks):
        task = tasks.pop(num - 1)
        print(f"Task '{task['name']}' deleted.")
    else:
        print("Invalid task number.")
while True:
    print("\n1. Show tasks\n2. Add task\n3. Complete task\n4. Delete task\n5. Exit")
    option = input("Choose an option: ")

    if option == '1':
        show_tasks()
    elif option == '2':
        task_name = input("Task name: ")
        add_task(task_name)
    elif option == '3':
        show_tasks()
        task_num = int(input("Task number to complete: "))
        complete_task(task_num)
    elif option == '4':
        show_tasks()
        task_num = int(input("Task number to delete: "))
        delete_task(task_num)
    elif option == '5':
        break
    else:
        print("Invalid option.")
