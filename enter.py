import tkinter as tk
from tkinter import *
from functools import partial



def clear_frame(root):        
    for widget in root.winfo_children():
        widget.destroy()
    return

class LoginForm:
    def __init__(self, root):
        self.root = root
        root.title('Enter')

        self.username_label = tk.Label(self.root, text = 'Username: ')
        self.username_label.grid(row = 0, column = 0)
        self.username = tk.StringVar()
        self.username_entry = tk.Entry(self.root, textvariable=self.username)
        self.username_entry.grid(row = 0, column = 1)

        self.password_label = tk.Label(self.root, text = 'Password: ')
        self.password_label.grid(row = 1, column = 0)
        self.password = tk.StringVar()
        self.password_entry = tk.Entry(self.root, textvariable=self.password, show='*')
        self.password_entry.grid(row = 1, column = 1)

        self.register_button = tk.Button(self.root, text = 'next', command=self.validate_login)
        self.register_button.grid(row = 3, column = 0, columnspan = 2)
        self.exit_button = tk.Button(self.root, text = 'create account', command=self.ext)
        self.exit_button.grid(row = 3, column = 2, columnspan = 2)
        return

    def ext(self):
        clear_frame(self.root)
        app = RegistrationForm(self.root)
        return

    def validate_login(self):
        pass


class RegistrationForm:
    def __init__(self, root):
        self.root = root
        self.root.title('Registration')

        self.username_label = tk.Label(self.root, text = 'username: ')
        self.username_label.grid(row = 0, column = 0)
        self.username = tk.StringVar()
        self.username_entry = tk.Entry(self.root, textvariable=self.username)
        self.username_entry.grid(row = 0, column = 1)
        
        self.username_sub_label = tk.Label(self.root, text = 'password characters should have only this characters A-Z, a-z, 0-9, and _')
        self.username_sub_label.grid(row = 1, column = 1)         

        self.password_label = tk.Label(self.root, text = 'password: ')
        self.password_label.grid(row = 2, column = 0)
        self.password = tk.StringVar()
        self.password_entry = tk.Entry(self.root, textvariable=self.password, show = '*')
        self.password_entry.grid(row = 2, column = 1)
        
        self.password_sub_label = tk.Label(self.root, text = 'password characters should have only this characters A-Z, a-z, 0-9, and _')
        self.password_sub_label.grid(row = 3, column = 1)

        self.confirm_password_label = tk.Label(self.root, text = 'confirm password: ')
        self.confirm_password_label.grid(row = 4, column = 0)
        self.confirm_password = tk.StringVar()
        self.confirm_password_entry = tk.Entry(self.root, textvariable=self.confirm_password, show = '*')
        self.confirm_password_entry.grid(row = 4, column = 1)
        
        self.confirm_password_sub_label = tk.Label(self.root, text = 'please repeat the password')
        self.confirm_password_sub_label.grid(row = 5, column = 1)

        self.register_button = tk.Button(self.root, text = 'next', command=self.validate_registration)
        self.register_button.grid(row = 6, column = 0, columnspan = 2)
        self.exit_button = tk.Button(self.root, text = 'have an account', command=self.ext)
        self.exit_button.grid(row = 6, column = 2, columnspan = 2)
        return

    def ext(self):
        clear_frame(self.root)
        app = LoginForm(self.root)
        return

    def validate_registration(self):
        pass

def enter(root):
    LoginForm(root)
    return

root = tk.Tk()
enter(root)
root.mainloop()
