'''
Overview:

In this project, you will build a functional To-Do List Application using
Python from scratch. This assignment will help you strengthen your 
understanding of Python concepts such as syntax, data types, control 
structures, functions, and error handling, all while creating a practical,
interactive command-line application.

Project:

In VS Code, create a .py file and complete the following requirements:

User Interface (UI) and Storage Method:

Build a simple Command Line Interface (CLI) that welcomes users and displays
a menu with options to add, view, delete tasks, or quit the application.
The tasks should be stored in a Python list.

Core Features:

- Add tasks
- View tasks
- Delete tasks
- Quit the application

User Interaction:

Use input() to capture user selections and ensure proper input validation to
handle invalid choices.

Error Handling:

- Implement error handling using try, except, else, and finally blocks to 
    catch errors
- Alert the user if they provide invalid input
- Alert the user if there are no tasks to view
- Alert the user if they try to delete a task that doesn't exist
- Alert the user if they select an option on the main menu that doesn't
    exist
- Code Organization
- Organize your code into functions to improve clarity and maintainability. 
- Use descriptive function names and add comments/docstrings where necessary.
- Testing and Debugging
- Thoroughly test your application, considering edge cases such as empty 
    lists and invalid input.
'''
tasks = []

def add_tasks(tasks):
    task = input("Enter your task: ")
    tasks.append(task)
    print(f"Task - {task} was added to the list.")
    print(tasks)

def view_tasks(tasks):
        print(tasks)

def delete_tasks(tasks):
    task_to_remove = input("Which task do you want to remove:")
    for task in tasks:
        tasks.remove(task)
        print(f"{task} was removed from todays tasks.")
        print(tasks)
        

def quit_application():
    print("Exiting the program.")
    exit()
    
def main():
    while True:
        print("\nTo Do Application")
        print("1. Add Tasks")
        print("2. View Tasks")
        print("3. Delete Tasks")
        print("4. Quit Application")
        try:      
            choice = input("Enter your choice: ")
    
            if choice == '1':
                add_tasks(tasks)
            elif choice == '2':
                view_tasks(tasks)
            elif choice == '3':
                delete_tasks(tasks)       
            elif choice == '4':
                quit_application()
                break
            else:
             print("Invalid Choice. Please select 1 through 4.")
        except ValueError as e:
            print("Please enter a valid number.")
        
if __name__=="__main__":
    main()
        
        
    