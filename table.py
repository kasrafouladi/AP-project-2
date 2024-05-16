from tabulate import tabulate
import os

table_data = [
    ["", "backlog", "todo", "doing", "done", "archived"],
    ["1", [], [], [], [], []],
    ["2", [], [], [], [], []],
    ["3", [], [], [], [], []],
    ["4", [], [], [], [], []],
    ["5", [], [], [], [], []],
    ["6", [], [], [], [], []],
    ["7", [], [], [], [], []],
    ["8", [], [], [], [], []],
    ["9", ["hamta"], [], [], [], []],
    ["10", [], [], [], [], []]
]

def move_tasks():
    try:
        display_table()
        number = input("""
1-move tasks
2-edit or add tasks
3-back
Enter a number: 
                       """)
        if number == "1":
            source_column = int(input("Enter the column number of the source task (1-5): "))
            source_row = int(input("Enter the row number of the source task (1-10): "))
            destination_column = int(input("Enter the column number of the destination task (1-5): "))
            destination_row = int(input("Enter the row number of the destination task (1-10): "))
            
            if 1 <= source_column <= 5 and 1 <= source_row <= 10 and 1 <= destination_column <= 5 and 1 <= destination_row <= 10:
                if table_data[source_row][source_column]:
                    table_data[destination_row][destination_column] = table_data[source_row][source_column]
                    table_data[source_row][source_column] = []
                    display_table()
                else:
                    print("Source task does not exist. Please try again.")
            else:
                print("Invalid row or column number. Please try again.")
        elif number == "2":
            while add_task():
                pass
        else:
            return
    except ValueError:
        print("Invalid input. Please enter valid row and column numbers.")

def display_table():
    headers = ["", "backlog", "todo", "doing", "done", "archived"]
    rows = []
    for i, row in enumerate(table_data[1:], start=1):
        rows.append([str(i)] + [", ".join(task) if task else "" for task in row[1:]])

    print(tabulate(rows, headers=headers, tablefmt='fancy_grid'))

def add_task():
    try:
        row = input("Enter row number (1-10) or type 'exit' to quit: ")
        if row.lower() == 'exit':
            return False
        
        row = int(row)
        column = int(input("Enter column number (1-5): "))
        task_name = input("Enter task: ")
        author_name = input("Enter author's name: ")

        if 1 <= row <= 10 and 1 <= column <= 5:
            table_data[row][column] = [task_name, author_name]
            display_table()
        else:
            print("Invalid row or column number. Please try again.")
        
        return True
    except ValueError:
        print("Invalid input. Please enter valid row and column numbers.")
        return True

def main_menu():
    while True:
        display_table()
        action = input("Select an action:\n1. Move tasks\n2. Edit or add tasks\n3. Exit\nEnter a number: ")
        if action == '1':
            move_tasks()
        elif action == '2':
            while add_task():
                pass
        elif action == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

main_menu()