from tabulate import tabulate
import os
import datetime
import basic as b

table_data = [
    ["", "backlog", "todo", "doing", "done", "archived"],
    ["1", {}, {}, {}, {}, {}],
    ["2", {}, {}, {}, {}, {}],
    ["3", {}, {}, {}, {}, {}],
    ["4", {}, {}, {}, {}, {}],
    ["5", {}, {}, {}, {}, {}],
    ["6", {}, {}, {}, {}, {}],
    ["7", {}, {}, {}, {}, {}],
    ["8", {}, {}, {}, {}, {}],
    ["9", {}, {}, {}, {}, {}],
    ["10", {}, {}, {}, {}, {}]
]

#############################################################################################

def log_history(action, details, path = "history.txt"):
    with open(path, 'a') as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{timestamp} - {action}: {details}\n")

#############################################################################################

def save_table(path="tabledata.txt"):
    with open(path, 'w') as f:
        for row in table_data:
            row_data = ["|".join(f"{k}:{v}" for k, v in task.items()) if isinstance(task, dict) else task for task in row]
            f.write("\t".join(row_data) + "\n")

#############################################################################################

def load_table(path="tabledata.txt"):
    if os.path.exists(path):
        with open(path, 'r') as f:
            lines = f.readlines()
            for i in range(1, len(table_data)):
                if i < len(lines):
                    row_data = lines[i].strip().split("\t")
                    for j in range(1, len(table_data[0])):
                        if j < len(row_data):
                            if ":" in row_data[j]:
                                tasks = row_data[j].split("|")
                                table_data[i][j] = {kv.split(":")[0]: kv.split(":")[1] for kv in tasks}
                            else:
                                table_data[i][j] = {} if row_data[j] == "" else row_data[j]
                        else:
                            table_data[i][j] = {}
                else:
                    for j in range(1, len(table_data[0])):
                        table_data[i][j] = {}

#############################################################################################

def find_first_empty_row(column):
    for row in range(1, len(table_data)):
        if not table_data[row][column]:
            return row
    return None

#############################################################################################

def move_tasks(path):
    try:
        display_table()
        source_column = int(input("Enter the column number of the source task (1-5): "))
        source_row = int(input("Enter the row number of the source task (1-10): "))
        destination_column = int(input("Enter the column number of the destination task (1-5): "))
        if 1 <= source_column <= 5 and 1 <= source_row <= 10 and 1 <= destination_column <= 5:
            if table_data[source_row][source_column]:
                destination_row = find_first_empty_row(destination_column)
                if destination_row is not None:
                    task = table_data[source_row][source_column]
                    table_data[destination_row][destination_column] = task
                    table_data[source_row][source_column] = {}
                    save_table(path + 'table.txt')
                    log_history("Move Task", b.user_handle + f" moved task {task} from ({source_row}, {source_column}) to ({destination_row}, {destination_column})", path + 'history.txt')
                    
                    b.os.rename(path + str(source_row) + '-' + str(source_column) + '.txt', path + str(source_row) + '-' + str(source_column) + '0.txt')
                    b.os.rename(path + str(destination_row) + '-' + str(destination_column) + '.txt', path + str(source_row) + '-' + str(source_column) + '.txt')
                    b.os.rename(path + str(source_row) + '-' + str(source_column) + '0.txt', path + str(destination_row) + '-' + str(destination_column) + '.txt')

                    display_table()
                else:
                    print("No empty row found in the destination column.")
            else:
                print("Source task does not exist. Please try again.")
        else:
            print("Invalid row or column number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter valid row and column numbers.")

#############################################################################################

def display_table():
    b.head()
    headers = ["", "backlog", "todo", "doing", "done", "archived"]
    rows = []
    for i, row in enumerate(table_data[1:], start=1):
        row_content = []
        for cell in row[1:]:
            if isinstance(cell, dict) and cell:
                cell_content = f" subject: {cell.get('subject', '')}\ntask:{cell.get('task', '')}\nfor: {cell.get('for', '')}\nauthor: {cell.get('author', '')}\nimp: {cell.get('imp', '')}"
                row_content.append(cell_content)
            else:
                row_content.append("")
        rows.append([str(i)] + row_content)

    print(tabulate(rows, headers=headers, tablefmt='fancy_grid'))

##############################################################################################

def add_task(path):
    try:
        row = input("Enter row number (1-10) or type 'exit' to quit: ")
        if row.lower() == 'exit':
            return

        row = int(row)
        column = int(input("Enter column number (1-5): "))
        subject = input("Enter subject: ")
        task_name = input("Enter task: ")
        for_whom = input("Enter assigned: ")
        author_name = b.user_handle
        imp = input("Improtance(1/2/3/4): ")
        dl = input("enter the deadline:")
        if 1 <= row <= 10 and 1 <= column <= 5:
            table_data[row][column] = {"task": task_name, "for": for_whom,
            "author": author_name, "subject": subject, "imp" : imp, "deadline" :  dl}
            save_table(path + 'table.txt')
            log_history("Add Task", b.user_handle + f" added task {table_data[row][column]} to ({row}, {column})", path + 'history.txt')
            display_table()
        else:
            print("Invalid row or column number. Please try again.")
        return

    except ValueError:
        print("Invalid input. Please enter valid row and column numbers.")
        return True

#####################################################################################################

def edit_task(path, al):
    try:
        row = int(input("Enter the row number of the task to edit (1-10): "))
        column = int(input("Enter the column number of the task to edit (1-5): "))

        if 1 <= row <= 10 and 1 <= column <= 5:
            if table_data[row][column]:
                print("Current task details:")
                print(f"Subject: {table_data[row][column].get('subject', '')}")
                print(f"Task: {table_data[row][column].get('task', '')}")
                print(f"For: {table_data[row][column].get('for', '')}")
                print(f"imp: {table_data[row][column].get('imp', '')}")
                print(f"deadline: {table_data[row][column].get('deadline', '')}")

                for_whom = ""
                dl = ""

                task_name = input("Enter new task name (leave blank to keep current): ")
                
                if b.user_handle == table_data[row][column].get('author', '') or al == 5:
                    for_whom = input("Enter new for (leave blank to keep current): ")
                
                imp = input("Enter new imp (leave blank to keep current): ")
                subject = input("Enter new subject (leave blank to keep current): ")

                if b.user_handle == table_data[row][column].get('author', '') or al == 5:
                    dl = input("Enter new deadline (leave blank to keep current): ")
                
                if dl:
                    table_data[row][column]['deadline'] = dl
                if task_name:
                    table_data[row][column]['task'] = task_name
                if for_whom:
                    table_data[row][column]['for'] = for_whom
                if imp:
                    table_data[row][column]['imp'] = imp
                if subject:
                    table_data[row][column]['subject'] = subject

                save_table(path + 'table.txt')
                log_history("Edit Task", b.user_handle + f" edited task at ({row}, {column}) to {table_data[row][column]}", path+'history.txt')
                display_table()
            else:
                print("No task found at the specified location.")
        else:
            print("Invalid row or column number. Please try again.")

    except ValueError:
        print("Invalid input. Please enter valid row and column numbers.")

def add_comment(path):
    b.head()
    s = input("to see the comments for a task please enter the tasks coordinate in table like this: x-y or enter -1 for back\n")
    if s == '-1':
        return
    b.head()
    f = open(path + s + '.txt', 'r')
    b.bold()
    print("Here you can read the comments about this task:\n\n")
    b.bold(False)
    print(f.read())
    f.close()
    comm = input("share your comment(or just press enter): ")
    if not comm:
        return
    f = open(path + s + '.txt', 'a')
    f.write('_' * 40 + "\nTime: " + b.time.ctime() + '\n')
    f.write(b.user_handle + ": " + comm + '\n')
    f.close()
    

    print("press any key to continue")
    b.getch()

def main_menu(path, al):
    load_table(path + 'table.txt')
    while True:
        display_table()
        action = input("Select an action:\n1. Move tasks\n2. Add tasks\n3. Edit tasks\n4. Add Comment\n5. Exit\n6. log\nEnter a number: ")

        if action == '1':
            move_tasks(path)

        elif action == '2':
            if 3 <= al:
                add_task(path)
            else:
                print("youre acess level is under 3 so yo cant add a task")

        elif action == '3':
            if 4 <= al:
                edit_task(path, al)
            else:
                print("youre acess level is under 4 so yo cant edit a task")

        elif action == '4':
            if 2 <= al:
                add_comment(path)
            else:
                print("youre acess level is under 2 so yo cant share your comment for a task")

        elif action == '5':
            print("Exiting program...")
            break

        elif action == '6':
            f = open(path + "history.txt", "r")
            print(f.read())
            print("press any key to continue")
            b.getch()
        
if __name__ == '__main__':
    b.user_handle = 'kasra'
    main_menu("a/", 5)