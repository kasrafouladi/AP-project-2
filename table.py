from tabulate import tabulate
import os
import basic as b
import account
import project

table_data = []

def ready():
    table_data = [] * 6
    table_data[0] = ["", "backlog", "todo", "doing", "done", "archived"]
    for i in range(1, 6):
        table_data[i] = [] * 10
        table_data[i][j] = i
        for j in range(1, 10):
            table_data[i][j] = ["", "", ""]            

def move_tasks(path):
    try:
        source_column = int(input("Enter the column number of the source task (1-5): "))
        source_row = int(input("Enter the row number of the source task (1-10): "))
        destination_column = int(input("Enter the column number of the destination task (1-5): "))
        destination_row = int(input("Enter the row number of the destination task (1-10): "))
        
        if 1 <= source_column <= 5 and 1 <= source_row <= 10 and 1 <= destination_column <= 5 and 1 <= destination_row <= 10:
            if table_data[source_row][source_column]:
                table_data[destination_row][destination_column] = table_data[source_row][source_column]
                table_data[source_row][source_column] = []
                display_table(path)
            else:
                print("Source task does not exist. Please try again.")
        else:
            print("Invalid row or column number. Please try again.")
        
    except ValueError:
        print("Invalid input. Please enter valid row and column numbers.")

def display_table(path):
    headers = ["", "backlog", "todo", "doing", "done", "archived"]
    rows = []
    for i, row in enumerate(table_data[1:], start=1):
        rows.append([str(i)] + [", ".join(task) if task else "" for task in row[1:]])
    
    print(tabulate(rows, headers=headers, tablefmt='fancy_grid'))
    pass#edit kon


def add_task(path):
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
            display_table(path)
        else:
            print("Invalid row or column number. Please try again.")
        
        return True
    
    except ValueError:
        print("Invalid input. Please enter valid row and column numbers.")
        return True


def edit_task(path):
    try:
        row = int(input("Enter the row number of the task to edit (1-10): "))
        column = int(input("Enter the column number of the task to edit (1-5): "))
        
        
        
        if table_data[row][column] != "":
            if 1 <= row <= 10 and 1 <= column <= 5:
                if table_data[row][column]:
                    task_name = input("Enter new task name: ")
                    author_name = input("Enter new author's name: ")
                    table_data[row][column] = [task_name, author_name]
                    display_table()
                else:
                    print("No task found at the specified location.")
            else:
                print("Invalid row or column number. Please try again.")
        
        
    except ValueError:
        print("Invalid input. Please enter valid row and column numbers.")


def save_it(path):
    s = ""
    for i in range(1, 11):
        for j in range(1, 6):
            for k in range(3):
                s += table_data[i][j][k]
                s += "\n#"
    with open(path, 'w') as f:
        f.write(s)
        f.close()
    
def read_it(path):
    lst = []
    with open(path, 'r') as f:
        lst = f.read().split('#')
    idx = 0
    for i in range(1, 6):
        for j in range(1, 11):
            for k in range(3):
                table_data[i][j][k] = lst[idx]
                idx += 1

def ready():
    table_data = [] * 6
    table_data[0] = ["", "backlog", "todo", "doing", "done", "archived"]
    
    for i in range(1, 6):
        table_data[i] = [] * 10
        table_data[i][j] = [i, "kasi", "author"]
        for j in range(1, 10):
            table_data[i][j] = ["", "", ""]

def main_menu(path):
    ready()
    read_it(path)
    while True:
        b.head()
        b.bold()
        display_table(path)
        action = input("Select an action:\n1. Move tasks\n2. Add tasks\n3. Edit tasks\n4. Exit\nEnter a number: ")
        
        if action == '1':
            move_tasks(path)
            
        elif action == '2':
            while add_task(path):
                pass
            
        elif action == '3':
            edit_task(path)
            with open(path, "w", encoding="utf-8") as file:
                file.write(tabulate(table_data, headers="firstrow", tablefmt='fancy_grid'))
            
        elif action == '4':
            print("Exiting program...")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")
    save_it(path)