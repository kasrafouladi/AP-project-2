import tkinter as tk
from functools import partial

class LoginForm:
    def __init__(self, root):
        self.root = root
        self.root.geometry('400x200')
        self.root.title('enter section')
        self.choice_label = tk.Label(root, text = "choose")
        self.choice_label.grid(row = 0, column = 0, columnspan = 2)
        self.register_button = tk.Button(root, text = "sign up", command = self.show_registration_form)
        self.register_button.grid(row = 1, column = 0)
        self.login_button = tk.Button(root, text = "sign in", command = self.show_login_form)
        self.login_button.grid(row = 1, column = 1)
        return

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        return

    def show_registration_form(self):
        self.clear_frame()
        return

    def show_login_form(self):
        self.clear_frame()
        return

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginForm(root)
    root.mainloop()