from tabulate import tabulate
import os
import basic as b
import account
import project

mxlen = 0

def move_tasks(path):
    try:
        source_column = int(input("Enter the column number of the source task (1-5): "))
        source_row = int(input("Enter the row number of the source task (1-10): "))
        destination_column = int(input("Enter the column number of the destination task (1-5): "))
        if 1 <= source_column <= 5 and 1 <= source_row <= 10 and 1 <= destination_column <= 5:
            if table_data[source_row][source_column]:
                swap([source_row, source_column], [source_row, destination_column])
                display_table(path)
            else:
                print("Source task does not exist. Please try again.")
        else:
            print("Invalid row or column number. Please try again.")
        
    except ValueError:
        print("Invalid input. Please enter valid row and column numbers.")

def display_table(path, table_data):
    mxlen = 4
    print('_' * 18 * (mxlen + 2))
    for i in range(6):
        print("|", end = '')
        print(table_data[0][i], end = '')
        print(' ' * (3 * mxlen - len(table_data[0][i])) + "|", end = '')
    print("")
    for i in range(1, 11):
        print('_' * 18 * (mxlen + 2))
        for k in range(3):
            print(' ' * (mxlen - len(table_data[i][0][k])) + "|", end = '')
            for j in range(1, 6):
                print("|", end = '')
                print(table_data[i][j][k], end = '')
                print(' ' * (mxlen - len(table_data[i][j][k])) + "|", end = '')
        print("")
    print('_' * 18 * (mxlen + 2))

def add_task(path):
    pass


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
                    display_table(path)
                else:
                    print("No task found at the specified location.")
            else:
                print("Invalid row or column number. Please try again.")        
    except ValueError:
        print("Invalid input. Please enter valid row and column numbers.")
    #edit kon

def save_it(path, table_data):
    s = ""
    for i in range(1, 11):
        for j in range(1, 6):
            for k in range(3):
                s += table_data[i][j][k]
                s += "\n#"
    with open(path, 'w') as f:
        f.write(s)
        f.close()
    
def read_it(path, table_data):
    mxlen = 10
    lst = []
    with open(path, 'r') as f:
        lst = f.read().split('#')
    idx = 0
    for i in range(1, 6):
        for j in range(1, 11):
            for k in range(3):
                table_data[i][j][k] = lst[idx]
                mxlen = max(mxlen, len(table_data[i][j][k]))
                idx += 1
    return table_data

def ready():
    mxlen = 10
    res = [""] * 6
    res[0] = ["", "backlog", "todo", "doing", "done", "archived"]
    for i in range(1, 6):
        res[i] = [""] * 11
        res[i][0] = [str(i), "kasi:", "author:"]
        for j in range(1, 11):
            res[i][j] = ["", "", ""]
    return res

def main_menu(path):
    table_data = ready()
    table_data = read_it(path, table_data)
    display_table(path, table_data)
    b.getch()
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
    save_it(path, table_data)
    
main_menu("init.txt")
b.head()
print('#' * 149)