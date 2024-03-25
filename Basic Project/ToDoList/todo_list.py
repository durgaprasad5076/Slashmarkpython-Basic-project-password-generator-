
class ToDoList:
    #Class constructor  to initialize the list of tasks
    def __init__(self):
        self.tasks=[]

    # Function to display the to-do list
    def display_tasks(self):
        print("\nMy TO-DO List:")
        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task['name']} - {'Completed' if task['completed'] else 'Not Completed'}")

    # Function to add a task to the to-do list
    def add_task(self):
        task_name=input("Enter the task name: ")
        self.tasks.append({"name": task_name, "completed": False})
        print(f"Task '{task_name}' added to my to-do list.")

    # Function to mark a task as completed
    def mark_completed(self):
        self.display_tasks()
        task_number = int(input("Enter the task number to mark as completed: "))
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1]['completed'] = True
            print(f"Task '{self.tasks[task_number - 1]['name']}' marked as completed.")
        else:
            print("Invalid task number.")

    # Function to remove a task from the to-do list
    def remove_task(self):
        self.display_tasks()
        task_number = int(input("Enter the task number to remove: "))
        if 1 <= task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Task '{removed_task['name']}' removed from the to-do list.")
        else:
            print("Invalid task number.")

def main():
    todoList=ToDoList()
    # Main program loop
    while True:
        print("\n TO-DO LIST MENU")
        print("1. Display to-do list")
        print("2. Add a task")
        print("3. Mark a task as completed")
        print("4. Remove a task")
        print("5. Quit\n")

        choice = int(input("Enter your choice: "))

        if choice ==1:
            todoList.display_tasks()
        elif choice ==2:
            todoList.add_task()
        elif choice == 3:
            todoList.mark_completed()
        elif choice == 4:
            todoList.remove_task()
        elif choice == 5:
            print("Exiting from the application.Thank you")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__=="__main__":
    main()
