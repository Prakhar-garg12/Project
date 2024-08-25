'''
                     Task 1
A To-Do List application is a useful project that helps users manage
and organize their tasks efficiently. This project aims to create a
command-line or GUI-based application using Python, allowing
users to create, update, and track their to-do lists
'''
class ToDoList:
    def __init__(self):
        self.tasks = {}

    def display_tasks(self):
        print("\nTo-Do List:")
        for task, status in self.tasks.items():
            print(f"{task}: {status}")

    def add_task(self):
        task = input("Enter task name: ")
        self.tasks[task] = "Pending"
        print("Task added successfully!")

    def update_task(self):
        task = input("Enter task name: ")
        if task in self.tasks:
            status = input("Enter new status (Pending/Done): ")
            self.tasks[task] = status
            print("Task updated successfully!")
        else:
            print("Task not found!")

    def delete_task(self):
        task = input("Enter task name: ")
        if task in self.tasks:
            del self.tasks[task]
            print("Task deleted successfully!")
        else:
            print("Task not found!")


def main():
    todo = ToDoList()
    while True:
        print("\n1. Display Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            todo.display_tasks()
        elif choice == "2":
            todo.add_task()
        elif choice == "3":
            todo.update_task()
        elif choice == "4":
            todo.delete_task()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()





