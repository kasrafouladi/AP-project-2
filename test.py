"""
import tkinter as tk

from tkinter import *

def clear_frame():
    for widget in window.winfo_children():
        widget.destroy()

def screen_two():
    clear_frame()
    button_2 = tk.Button(window, text = "Go to screen one", command = screen_one)
    button_2.place(relx = 0.75, rely = 0.5)
    label_2 = tk.Label(window, text = "Label on window two")
    #label_3 = tk.Label(window, image = r'cover.png')
    #label_3.place(relx = 0, rely=0, width="50%", height = "50%")
    label_2.place(relx = 0.1, rely = 0.1)

def screen_one():
    clear_frame()
    label_1 = tk.Label(window, text = "1")
    label_1.place(relx = 0.1, rely = 0.1)
    button_1 = tk.Button(window, text = "Go to screen two", font = ("calibri", 10), command = screen_two)
    button_1.place(relx = 0.75, rely = 0.5)

window = tk.Tk()
window.title("Screen Switching Example")

screen_one()  # نمایش صفحه اول
window.mainloop()



# Import module 
from tkinter import *

# Create object 
root = Tk() 

# Adjust size 
root.geometry("400x400") 

# Add image file 

# Show image using label 
label2 = Label( root, text = "Welcome") 
label2.pack(pady = 50) 

# Create Frame 
frame1 = Frame(root) 
frame1.pack(pady = 20 ) 

# Add buttons 
button1 = Button(frame1,text="Exit") 
button1["bg"] = "blue"
button1.pack(pady=20) 

button2 = Button( frame1, text = "Start") 
button2.pack(pady = 20) 

button3 = Button( frame1, text = "Reset") 
button3.pack(pady = 20) 

# Execute tkinter 
root.mainloop()
"""
import random
from tkinter import Tk, Label, Button, Entry, StringVar, DISABLED, NORMAL, END, W, E

class GuessingGame:
    def __init__(self, master):
        self.master = master
        master.title("Guessing Game")
        self.secret_number = random.randint(1, 100)
        self.guess = None
        self.num_guesses = 0
        self.message = "Guess a number from 1 to 100"
        self.label_text = StringVar()
        self.label_text.set(self.message)
        self.label = Label(master, textvariable=self.label_text)
        vcmd = master.register(self.validate)
        self.entry = Entry(master, validate = "key", validatecommand = (vcmd, '%P'))
        self.guess_button = Button(master, text="Guess", command=self.guess_number)
        self.reset_button = Button(master, text="Play again", command=self.reset, state=DISABLED)
        self.label.grid(row=0, column=0, columnspan=2, sticky=W+E)
        self.entry.grid(row=1, column=0, columnspan=2, sticky=W+E)
        self.guess_button.grid(row=2, column=0)
        self.reset_button.grid(row=2, column=1)

    def validate(self, new_text):
        if not new_text: # the field is being cleared
            self.guess = None
            return True

        try:
            guess = int(new_text)
            if 1 <= guess <= 100:
                self.guess = guess
                return True
            else:
                return False
        except ValueError:
            return False

    def guess_number(self):
        self.num_guesses += 1

        if self.guess is None:
            self.message = "Guess a number from 1 to 100"

        elif self.guess == self.secret_number:
            suffix = '' if self.num_guesses == 1 else 'es'
            self.message = "Congratulations! You guessed the number after %d guess%s." % (self.num_guesses, suffix)
            self.guess_button.configure(state=DISABLED)
            self.reset_button.configure(state=NORMAL)

        elif self.guess < self.secret_number:
            self.message = "Too low! Guess again!"
        else:
            self.message = "Too high! Guess again!"

        self.label_text.set(self.message)

    def reset(self):
        self.entry.delete(0, END)
        self.secret_number = random.randint(1, 100)
        self.guess = 0
        self.num_guesses = 0

        self.message = "Guess a number from 1 to 100"
        self.label_text.set(self.message)

        self.guess_button.configure(state=NORMAL)
        self.reset_button.configure(state=DISABLED)

root = Tk()
my_gui = GuessingGame(root)
root.mainloop()