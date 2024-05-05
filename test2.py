import tkinter as tk

def show_password():
    password = password_var.get()
    print("Entered password:", password)

root = tk.Tk()
root.title("Password Entry Example")

# Create a StringVar to store the password
password_var = tk.StringVar()

# Create an Entry widget for password input
password_entry = tk.Entry(root, textvariable=password_var, show = "*")
password_entry.pack(pady=10)

# Create a button to show the entered password
show_button = tk.Button(root, text="Show Password", command=show_password)
show_button.pack()

root.mainloop()
