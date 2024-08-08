def app(): # app() runs the program
    tasks = []
    try:
        while True:
            menu = input("""
            Welcome to the To-Do List App!
                            
            Menu:
            1. Add a task
            2. View tasks
            3. Mark a task as complete
            4. Delete a task
            5. Quit
                    
            Please enter a selection: """)

            if (menu) == "1":
                tasks = add_task(tasks)
            elif (menu) == "2":
                view_tasks(tasks)
            elif (menu) == "4":
                tasks = delete_task(tasks)
            elif (menu) == "5":
                break
            else:
                print("Sorry, that's not a valid input. Please try again.")
    except (OverflowError, TypeError, ValueError):
                print("Sorry, that's not a valid input. Please try again.")
    finally:
                print("Thank you for using this application. Goodbye!")
    return tasks

def add_task(tasks): # add_task() allows the user to add a task to the to-do list
    task = input("What task would you like to add? ")
    tasks.append(task)
    return tasks

def view_tasks(tasks): # view_tasks() allows the user to view the to-do list
    if tasks:
        print(f"Current to-do list: {tasks}")
    else:
        print("Current to-do list: empty.")

def delete_task(tasks): # delete_task() allows the user to remove a task from the to-do list
    delete = input("Which task would you like to delete? ")
    if delete in tasks:
        tasks.remove(delete)
    else:
        print(f"Sorry, {delete} isn't one of the tasks on the list. Please try again.")
    return tasks

def quit(): # quit() exits the application
    print("Thank you for using this application. Goodbye!")

app()