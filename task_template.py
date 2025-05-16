def register_user():
    if current_user != "admin":
        print("Only admin can register new users.")
        return

    username = input("Enter new username: ")
    password = input("Enter new password: ")
    confirm_password = input("Confirm password: ")
    if password == confirm_password:
        with open("user.txt", "a") as f:
            f.write(f"{username}, {password}\n")
            print("User registered successfully")
    else:
        print("Passwords do not match")

def add_task():
    task_username = input("Enter the username of whom the task is assigned to: ")
    task_title = input("Enter the title of the task: ")
    des_task = input("Enter a description of the task: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    current_date = input("Enter current date (YYYY-MM-DD): ")  # User inputs current date

    # Open the file in append mode and check for existing content
    with open("tasks.txt", "a+") as f:
        f.seek(0)  # Move to the beginning of the file to check content
        if f.read(1):  # Check if file is not empty
            f.seek(0, 2)  # Move to the end of the file
            if not f.tell() or f.read(1) != '\n':  # Check if last character is not a newline
                f.write("\n")  # Add a newline if necessary
        f.write(f"{task_username}, {task_title}, {des_task}, {current_date}, {due_date}, No\n")
    print("Task added")

def view_all_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        print("\nAll Tasks:")
        for task in tasks:
            task_data = task.strip().split(", ")
            print(f"""
Task assigned to: {task_data[0]}
Title: {task_data[1]}
Description: {task_data[2]}
Current Date: {task_data[3]}
Due Date: {task_data[4]}
Completed: {task_data[5]}
""")
    except FileNotFoundError:
        print("No tasks found. Please add tasks first.")

def view_my_tasks(username):
    found = False
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        print(f"\nTasks assigned to {username}:")
        for task in tasks:
            task_data = task.strip().split(", ")
            if task_data[0] == username:
                found = True
                print(f"""
Title: {task_data[1]}
Description: {task_data[2]}
Current Date: {task_data[3]}
Due Date: {task_data[4]}
Completed: {task_data[5]}
""")
        if not found:
            print("No tasks assigned to you.")
    except FileNotFoundError:
        print("No tasks found. Please add tasks first.")

def display_statistics():
    try:
        with open("tasks.txt", "r") as task_file:
            tasks = task_file.readlines()
        with open("user.txt", "r") as user_file:
            users = user_file.readlines()
        
        total_tasks = len(tasks)
        total_users = len(users)

        print(f"\nTotal number of tasks: {total_tasks}")
        print(f"Total number of users: {total_users}")
    except FileNotFoundError:
        print("Could not find the necessary files.")

def login():
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        try:
            with open("user.txt", "r") as file:
                users = file.readlines()
                for user in users:
                    user_data = user.strip().split(", ")
                    if username == user_data[0] and password == user_data[1]:
                        print(f"Welcome, {username}!")
                        return username
                print("Error was found, try again.")
        except FileNotFoundError:
            print("User file not found.")

current_user = login()

while True:
    menu = input('''\nSelect one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
s - display statistics (admin only)
e - exit
: ''').lower()
    if menu == 'r':
        register_user()
    elif menu == 'a':
        add_task()
    elif menu == 'va':
        view_all_tasks()
    elif menu == 'vm':
        view_my_tasks(current_user)
    elif menu == 's' and current_user == "admin":
        display_statistics()
    elif menu == 'e':
        print('Goodbye!')
        break
    else:
        print("Invalid input. Please try again.")