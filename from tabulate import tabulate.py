from tabulate import tabulate
import os

# ساختار داده‌ای برای جدول
columns = ["Todo", "Doing", "Done", "Backlog", "Archived"]
tasks = {column: [["", "", ""] for _ in range(10)] for column in columns}

# ذخیره‌سازی جدول در فایل
def save_to_file():
    with open("tasks.txt", "w") as file:
        for i in range(10):
            row = []
            for column in columns:
                task = tasks[column][i]
                formatted_task = "\n".join(task)
                row.append(formatted_task)
            file.write(tabulate([row], headers=columns, tablefmt="grid"))
            file.write("\n")

# بارگذاری جدول از فایل
def load_from_file():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            lines = file.readlines()
            current_column = 0
            current_row = 0
            for line in lines:
                if "+" in line or "-" in line:
                    continue
                cells = line.split("|")[1:-1]
                for idx, cell in enumerate(cells):
                    task_parts = cell.strip().split("\n")
                    tasks[columns[idx]][current_row] = task_parts + [""] * (3 - len(task_parts))
                current_row += 1
                if current_row == 10:
                    current_row = 0

# افزودن وظیفه جدید
def add_task(column, row, task):
    tasks[column][row] = task
    save_to_file()

# ویرایش وظیفه
def edit_task(column, row, task):
    tasks[column][row] = task
    save_to_file()

# جابجایی وظیفه
def move_task(from_column, from_row, to_column, to_row):
    tasks[to_column][to_row] = tasks[from_column][from_row]
    tasks[from_column][from_row] = ["", "", ""]
    save_to_file()

# نمایش منو
def show_menu():
    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Edit Task")
        print("3. Move Task")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            column = input("Enter column (Todo/Doing/Done/Backlog/Archived): ")
            row = int(input("Enter row (0-9): "))
            task = [
                input("Enter Task: "),
                input("Enter Author: "),
                input("Enter To: ")
            ]
            add_task(column, row, task)

        elif choice == "2":
            column = input("Enter column (Todo/Doing/Done/Backlog/Archived): ")
            row = int(input("Enter row (0-9): "))
            task = [
                input("Enter Task: "),
                input("Enter Author: "),
                input("Enter To: ")
            ]
            edit_task(column, row, task)

        elif choice == "3":
            from_column = input("Enter from column (Todo/Doing/Done/Backlog/Archived): ")
            from_row = int(input("Enter from row (0-9): "))
            to_column = input("Enter to column (Todo/Doing/Done/Backlog/Archived): ")
            to_row = int(input("Enter to row (0-9): "))
            move_task(from_column, from_row, to_column, to_row)

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please try again.")

        print("\nCurrent Tasks:")
        print(tabulate([[f"{task[0]}\n{task[1]}\n{task[2]}" for task in row] for row in zip(*[tasks[column] for column in columns])], headers=columns, tablefmt="grid"))

if __name__ == "__main__":
    load_from_file()
    show_menu()
