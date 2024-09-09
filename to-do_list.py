# Mini-Project: The to-do list application

'''
Introduction: In this project, I will apply python skills to create a functional to-do list Application from scratch.
The objective is to reinforce the understanding of python syntax, data types, control structures, functions and error handling while building a practical and interactive application.

**Project Requirements**

1. User interface (UI)
* Create a command-line interface (CLI) for the to-do list application.
* Display a welcoming message and a menu with the following options:
    Welcome to the to-do list app!

    Menu:
    1. Add a task
    2. View tasks
    3. Mark a task as complete
    4. Delete a task
    5. Quit

2. to-do list features:
    * Implement the following features:

    -Adding a task with a title (by default "incomplete").
    -Viewing the list of tasks with their totles and statuses (e.g., "Incomplete" or "Complete").
    - Marking a task as Complete.
    -Deleting a task.
    - Quiting the application.

3. User interaction:

    -Allow the user to interact with the application by selecting menu options using input().
    -Implement input validation to handle unexpected user input gracefully.

4. Error Handling:

    -Implement eror handling using try, except, else, and finally blocks to handle potential issues.

5. Code organization:

    - Orginize your code into functions to promote modularity and readabillity.
    - Use meaningful functionn names with appropiate comments and docstrings for clarity.

6. Testing and Debuging:
    - Thoroughly test your application to identify and fix bugs.
    - Consider edge cases, such as empty tasks list or incorrect user input.


7. Documentation:
    - Include a README file that explains how to run the application and provides a brief overview of its features.


8. Optional Features (Bonus):
    - If you feel adventurous, you can add extra features like task priorities, due dates, or color-coding tasks based on their status.


9. GitHub Repository:

    -Create a GitHub repository for your project.
    -Commit your repository regularly.
    - Include a link to your GitHub repository in your project documentation.
'''


complete_tasks = ['laundry','call sister', 'download file']
incomplete_tasks = ['hit the gym','deliver assignment']
def To_do_list(complete_tasks, incomplete_tasks):

    try:


        while True:
            print("Menu")
            print("1. Add s Task")
            print("2. View Tasks")
            print("3. Mark task as Complete")
            print("4. Delete a task")
            print("5. Quit")
            user_choice = input("Enter your choice:")

            if user_choice == '1':
                incomplete = input("What is the new task you wish to create?:")
                incomplete = incomplete_tasks.append(incomplete)
                print(f" The task {incomplete} has been added to the incompleted list")

            elif user_choice == '2':
                for task in complete_tasks[:-1] and incomplete_tasks[:-1]:
                    print(f"The complete tasks are:{complete_tasks} and incomplete tasks are:{incomplete_tasks}")

            elif user_choice == '3':
# To mark a task as complete i need to swap from one list into another one and print the changed item
                marked_task = input("What task do you want to mark as completed?:")
                if marked_task in incomplete_tasks:
                    complete_tasks.append(marked_task)
                    if marked_task in incomplete_tasks:
                        incomplete_tasks.remove(marked_task)
                    print(f"The task {marked_task} has been marked as completed.")

            elif user_choice == '4':
                unwanted_task = input("Delete as task:")
                if unwanted_task in complete_tasks:
                    complete_tasks.remove(unwanted_task)
                    print(f"{unwanted_task} has been deleted form the list of tasks.")
                elif unwanted_task in incomplete_tasks:
                    incomplete_tasks.remove(unwanted_task)
                    print(f"{unwanted_task} has been deleted from the list of tasks.")

            elif user_choice == '5':
                print("Exiting the to-do list.")
                break

            else:
                print("Unexpected value entered, please select an option 1 o 5.")    



    except Exception as e:
            print(f"An error has ocurred: {e}, Please try again!")
            

    else:
        print("If you wish to use the to-do list again, hit down and enter")
    

        
    finally:
        print("Thanks for using this to-do list!")
        


    
To_do_list(complete_tasks, incomplete_tasks)