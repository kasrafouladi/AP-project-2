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
        self.root.title('Sign in')
        
        self.username_label = tk.Label(root, text = 'username: ')
        self.username_label.grid(row = 0, column = 0)
        self.username = tk.StringVar()
        self.username_entry = tk.Entry(root, textvariable=self.username)
        self.username_entry.grid(row = 0, column = 1)

        self.password_label = tk.Label(root, text = 'password: ')
        self.password_label.grid(row = 1, column = 0)
        self.password = tk.StringVar()
        self.password_entry = tk.Entry(root, textvariable=self.password, show='*')
        self.password_entry.grid(row = 1, column = 1)

        self.register_button = tk.Button(root, text = 'next', command=self.validate_login)
        self.register_button.grid(row = 3, column = 0, columnspan = 2)
        self.exit_button = tk.Button(root, text = 'create account', command=self.ext)
        self.exit_button.grid(row = 3, column = 2, columnspan = 2)

    def ext(self):
        clear_frame(self.root)
        app = RegistrationForm(self.root)
        return

    def validate_login(self):
        if self.password.get() == self.confirm_password.get():
            print("نام کاربری:", self.username.get())
            print("رمز عبور:", self.password.get())
            # در اینجا منطق ثبت‌نام را پیاده‌سازی کنید
        else:
            print("رمز عبور و تأیید رمز عبور مطابقت ندارند!")


class RegistrationForm:
    def __init__(self, root):
        self.root = root
        self.root.geometry('400x200')
        self.root.title('Sign up')

        self.username_label = tk.Label(root, text = 'username: ')
        self.username_label.grid(row = 0, column = 0)
        self.username = tk.StringVar()
        self.username_entry = tk.Entry(root, textvariable=self.username)
        self.username_entry.grid(row = 0, column = 1)

        self.password_label = tk.Label(root, text = 'password: ')
        self.password_label.grid(row = 1, column = 0)
        self.password = tk.StringVar()
        self.password_entry = tk.Entry(root, textvariable=self.password, show='*')
        self.password_entry.grid(row = 1, column = 1)

        self.confirm_password_label = tk.Label(root, text = 'confirm password: ')
        self.confirm_password_label.grid(row = 2, column = 0)
        self.confirm_password = tk.StringVar()
        self.confirm_password_entry = tk.Entry(root, textvariable=self.confirm_password, show = '*')
        self.confirm_password_entry.grid(row = 2, column = 1)

        self.register_button = tk.Button(root, text = 'next', command=self.validate_registration)
        self.register_button.grid(row = 4, column = 0, columnspan = 2)
        self.exit_button = tk.Button(root, text = 'have an account', command=self.ext)
        self.exit_button.grid(row = 4, column = 2, columnspan = 2)

    def ext(self):
        clear_frame(self.root)
        app = LoginForm(self.root)
        return

    def validate_registration(self):
        if self.password.get() == self.confirm_password.get():
            print("نام کاربری:", self.username.get())
            print("رمز عبور:", self.password.get())
            # در اینجا منطق ثبت‌نام را پیاده‌سازی کنید
        else:
            print("رمز عبور و تأیید رمز عبور مطابقت ندارند!")

def ejra(root):
    app = RegistrationForm(root)
    root.mainloop()
    return