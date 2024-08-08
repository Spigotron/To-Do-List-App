def app(): # app() runs the program
    tasks = []

    try:
        while True:
            menu = input("""
                         
            Welcome to the To-Do List App!
                            
            Menu:
            1. Add a task
            2. View tasks
            3. Delete a task
            4. Quit
                    
            Enter a selection: """)

            if (menu) == "1":
                tasks = add_task(tasks)
            elif (menu) == "2":
                view_tasks(tasks)
            elif (menu) == "3":
                tasks = delete_task(tasks)
            elif (menu) == "4":
                break
            else:
                print("Sorry, that's not a valid selection.")

    except (OverflowError, TypeError, ValueError):
        print("Sorry, that's not a valid selection.")
    finally:
        print("Thank you for using this application. Have a nice day!")
    return tasks

def add_task(tasks): # add_task() allows the user to add a task to the to-do list
    task = input("What task would you like to add? ")
    tasks.append(task)
    print("Task added!")
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
        print("Task deleted!")
    else:
        print(f"Sorry, {delete} isn't one of the tasks on the list..")
    return tasks

def quit(): # quit() exits the application
    print("Thank you for using this application. Have a nice day!")

app()