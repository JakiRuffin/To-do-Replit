from typing import Literal

print("--To-Do List Manager--")
print("\n")
print("What would you like to do?")
print("1. Add task")
print("2. View task list")
add_task = 1
view_task = 2
print("\n")
#broken
task = 0
task_input = int()
input(f"Enter your choice: {task_input}")

task = task_input
#broke





# The words of the actual task
new_strings = str()

# Error if user inputs an inappropriate manager cmd
if task > 2:
    print("Invalid input")

# Add task
if task == 1:
    new_strings = input("New task name: ")
    print(f"Task added to the list: {new_strings}")

    print("\n")
    print("What is the priority of the task?")
    print("1. High")
    print("2. Medium")
    print("3. Low")
    print("\n")

    # Task priority prompt
    task_priority = int(input("Input: "))

    

    # Order of tasks on the list
    if task_priority == 1:
        task_1 = new_strings
        print(f"Priority 1 is now: {new_strings}")
    elif task_priority == 2:
        task_2 = new_strings
        print(f"Priority 2 is now: {new_strings}")
    elif task_priority == 3:
        task_3 = new_strings
        print(f"Priority 3 is now: {new_strings}")
    else:
        print("Invalid input")

    

# View task list

    



    
       
    
        

# Show task list
# Initialize task_1 with an empty string
task_1 = '' 
task_2 = ''
task_3 = ''

if task == 2:
    print("Here is your task list:")
    if 'task_1' in locals():
        print(f"1. {task_1}")
    if 'task_2' in locals():
        print(f"2. {task_2}")
    if 'task_3' in locals():
        print(f"3. {task_3}")


        

        
        
