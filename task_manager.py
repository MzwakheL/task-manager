#=====importing libraries===========
'''This is the section where you will import libraries'''
from datetime import datetime, date
import os
import sys

tasks = []

# Define function to register new users
def reg_user():
    while True:
        username = input("Enter a new username: ")
        with open("user.txt", "r+") as file:
            for line in file:
                if username == line.strip().split(", ")[0]:
                    print("Username already exists. Please choose a different username.")
                    break
            else:
                break

    password = input("Enter a password: ")
    confirm_password = input("Confirm password: ")
    while password != confirm_password:
        print("Passwords don't match. Please try again.")
        password = input("Enter a password: ")
        confirm_password = input("Confirm password: ")

    with open("user.txt", "a") as file:
        file.write(f"\n{username}, {password}")
    print(f"{username} has been added to user.txt")

# Define function to add tasks
def add_task():
    """
    Adds a new task to tasks.txt
    """
    task_user = input("Assign the task to whom (username): ")
    task_title = input("Enter the title of the task: ")
    task_desc = input("Enter the description of the task: ")
    task_due_date = input("Enter the due date of the task (dd-mmm-yyyy): ")
    date_assigned = date.today().strftime("%d-%b-%Y")
    task_status = "No"
    with open("tasks.txt", "a") as file:
        file.write(f"\n{task_user}, {task_title}, {task_desc}, {date_assigned}, {task_due_date}, {task_status}")
    print("\nTask added successfully!")


# Define function to view all tasks
def view_all():
    """
    Displays all tasks listed in tasks.txt
    """
    with open('tasks.txt', 'r') as file: # read tasks from file in read mode
        tasks = file.readlines()
        if len(tasks) == 0:
            print("No tasks found.")

        assigned_tasks = []
        for task in tasks:
            task = task.strip().split(',')
            if task[0] == username:
                assigned_tasks.append(task)

        if len(assigned_tasks) == 0:
            print("No tasks assigned to you.")

        print("\nTasks assigned to you:\n")
        for i, task in enumerate(assigned_tasks):
            print(f"{i+1}. Assigned by: {task[0]}")
            print(f"   Task title: {task[1]}")
            print(f"   Task description: {task[2]}")
            print(f"   Assigned date: {task[3]}")
            print(f"   Due date: {task[4]}")
            print(f"   Completed: {task[5]}")
            print("")


# Define function to view my tasks
def view_mine():
        # read tasks from file in read mode
        with open("tasks.txt", "r") as file:
            # Initialize an empty list to store the user's tasks
            all_tasks = []
            my_tasks = []

            # Loop through each line in the file
            for line in file:

                # Split the line into parts using the comma delimiter
                line_parts = line.strip().split(",")

                if len(line_parts) >= 6:  # Make sure there are at least 6 elements in line_parts

                    # Append the task to the all tasks list
                    all_tasks.append(line_parts)

                    # Check if the task is assigned to the current user
                    if line_parts[0] == username:
                        # Append the task to the user's list of tasks
                        my_tasks.append(line_parts)

            # Check if the user has any tasks
            if len(my_tasks) == 0:
                print("You have no tasks.")
                return

            # Print the user's tasks
            print("Your tasks:")
            for i, task in enumerate(my_tasks):
                print(f"{i+1}. {task[2]}, Due: {task[4]}, Completed: {task[5]}")

            while True:
                    # prompt the user to choose a task to edit
                    choice = input("\nEnter the number of the task you want to edit, or -1 to return to the main menu: ")
                    if choice == "-1":
                        break
                        
                    elif not choice.isdigit() or int(choice) < 1 or int(choice) > len(my_tasks):
                        print("\nInvalid choice. Please enter a valid number or -1.\n")
                        continue
                        
                    # get the chosen task
                    task_index = int(choice) - 1
                    task = my_tasks[task_index]

                    # check if the task has already been completed
                    if task[5] == 'Yes':
                        print("\nThis task has already been completed and cannot be edited.")
                        continue

                    # prompt the user to choose an edit option
                    edit_choice = input("Enter '1' to mark the task as complete, '2' to edit the due date, or '3' to edit the assignee: ")

                    if edit_choice == '1':
                        task[5] = 'Yes'
                        print("\nTask marked as complete.")
                    elif edit_choice == '2':
                        new_date = input("Enter the new due date in the format 'dd-mm-yyyy': ")
                        task[4] = new_date
                        print("\nDue date updated.")
                    elif edit_choice == '3':
                        new_user = input("Enter the username of the new assignee: ")
                        task[0] = new_user
                        print("\nAssignee updated.")
                
            with open("tasks.txt", "w") as file: # open the tasks file in write mode
                for task in all_tasks:
                    file.write(",".join(task) + "\n") # write the updated task back to the file

                else:
                    print("Invalid choice.")
        
# print a confirmation message
print("Task updated successfully!")


def generate_reports():
    # Open the tasks.txt file in read mode
    with open("tasks.txt", "r") as file:
        # Initialize counters for the different task statuses
        total_tasks = 0
        completed_tasks = 0
        incomplete_tasks = 0
        overdue_tasks = 0

        # Loop through each line in the file
        for line in file:
            # Split the line into parts using the comma delimiter
            line_parts = line.strip().split(", ")
            if len(line_parts) >= 6:  # Make sure there are at least 6 elements in line_parts
                # Check if the task is completed
                if line_parts[5] == "Yes":
                    completed_tasks += 1
                else:
                    incomplete_tasks += 1
                    # Check if the task is overdue
                    due_date = line_parts[4].strip()
                    if date.today().strftime("%d-%b-%Y") > due_date:
                        overdue_tasks += 1
                total_tasks += 1

       # Compute the percentages
        if total_tasks > 0:
            incomplete_percentage = incomplete_tasks / total_tasks * 100
            overdue_percentage = overdue_tasks / total_tasks * 100

    # code for generating user_overview.txt
    with open("user.txt", "r") as file:
        # code for generating user_overview.txt
        pass

    # Print the report to the console
    print(f"Task Overview:\n\nTotal tasks: {total_tasks}\nCompleted tasks: {completed_tasks}\nIncomplete tasks: {incomplete_tasks}\nOverdue tasks: {overdue_tasks}\nIncomplete task percentage: {incomplete_percentage:.2f}%\nOverdue task percentage: {overdue_percentage:.2f}%")


def display_statistics():
    total_tasks = 0
    completed_tasks = 0
    incomplete_tasks = 0
    overdue_tasks = 0
    
    with open("tasks.txt", "r") as file:
        for line in file:
            line_parts = line.strip().split(", ")
            if len(line_parts) >= 6:
                if line_parts[5].lower() == "yes":
                    completed_tasks += 1
                else:
                    incomplete_tasks += 1
                    due_date = line_parts[4].strip()
                    if  date.today().strftime("%d-%b-%Y") > due_date:
                        overdue_tasks += 1
                total_tasks += 1
    
    incomplete_percentage = incomplete_tasks / total_tasks * 100 if total_tasks > 0 else 0
    overdue_percentage = overdue_tasks / total_tasks * 100 if total_tasks > 0 else 0
    
    print("Task Manager Statistics")
    print("========================")
    print(f"Total tasks: {total_tasks}")
    print(f"Completed tasks: {completed_tasks}")
    print(f"Incomplete tasks: {incomplete_tasks}")
    print(f"Overdue tasks: {overdue_tasks}")
    print(f"Incomplete tasks percentage: {incomplete_percentage:.2f}%")
    print(f"Overdue tasks percentage: {overdue_percentage:.2f}%")



# This code will exit the program once the user has selected 'e'. 
def exit_program():
    print("\nExiting program...\n")
    sys.exit(0)  # Imported the sys module for this to work


#====Login Section====
''' Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''

# Asking for the correct username and password that is currently saved in the user.txt file.

login = False
while not login:
    username = input("\nEnter your username: ")
    password = input("Enter your password: ")

    with open("user.txt", "r") as file:
        for line in file:
            values = line.strip().split(", ")
            if len(values) == 2 and values[0] == username and values[1] == password:
                print("\nLogin successful!\n")
                login = True
                break
        else:
            print("\nIncorrect username or password.\n")


if login:
    while True:
        menu = input(f'''\nWelcome, {username}!
            Please select one of the following Options:
            r - register user
            a - add task
            va - view all tasks
            vm - view my tasks
            gr - generate reports
            ds - display statistics
            e - exit: \n''').lower() # .lower() will default all users input into lowercase. 

        if menu == 'r':
            reg_user()
        elif menu == 'a':
            add_task()
        elif menu == 'va':
            view_all()
        elif menu == 'vm':
            view_mine()
        elif menu == 'gr':
            generate_reports()
        elif menu == 'ds':
            display_statistics()
        elif menu == 'e':
            exit()
            break
        else:
            print("Invalid selection. Please try again.")

# ref - https://www.youtube.com/watch?v=-AlFiS74aQg
# ref - https://www.geeksforgeeks.org/python-datetime-strptime-function/ 
# ref - https://stackoverflow.com/questions/30112357/typeerror-descriptor-strftime-requires-a-datetime-date-object-but-received
# ref - https://www.freecodecamp.org/news/file-handling-in-python/#:~:text=Write%20and%20Read%20('w%2B,where%20the%20handle%20is%20located. 
# ref - https://stackoverflow.com/questions/4719438/editing-specific-line-in-text-file-in-python 