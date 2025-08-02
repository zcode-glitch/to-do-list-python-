# Welcome Message
print("====================================")
print("== Welcome In To Do List Terminal ==")
print("====================================")

# Main Function
def main():
    tasks = []
    while True:

        print(''' This Simple Aplication To Do List Terminal
        \n1. Add a task\n2. Remove a task\n3. View all tasks\n4. Mark Task as Done\n5. Exit the application\nPlease choose an option by entering the corresponding number.
            ''')
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            n_task = int(input("Many task you want to add: "))
            for i in range(n_task):
                task = input("Enter the task: ")
                tasks.append(task)
                print(f"Task '{task}' added successfully!")
            
        elif choice == 2:
            if not tasks:
                print("No tasks to remove.")
            else:
                print("Current tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
                task_index = int(input("Enter the number of the task you want to remove: ")) - 1
                if 0 <= task_index < len(tasks):
                    removed_task = tasks.pop(task_index)
                    print(f"Task '{removed_task}' removed successfully!")
                else:
                    print("Invalid task number.")
                    
        elif choice == 3:
            if not tasks:
                print("No tasks available.")
            else:
                print("Current tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
                    
        elif choice == 4:
            if not tasks:
                print("No tasks to mark as done.")
            else:
                print("Current tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
                task_index = int(input("Enter the number of the task you want to mark as done: ")) - 1
                if 0 <= task_index < len(tasks):
                    done_task = tasks[task_index]
                    print(f"Task '{done_task}' marked as done!")
                    tasks.pop(task_index)
                else:
                    print("Invalid task number.")
                    
        elif choice == 5:
            print("Exiting the application. Goodbye!")
            print("== Please Support My Github ZCode ==\nWith Give Me A Star In All My Projcts\nThanks All")
            break
        
if __name__ == "__main__":
    main()