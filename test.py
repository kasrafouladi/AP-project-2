import tkinter as tk

def clear_frame():
    for widget in window.winfo_children():
        widget.destroy()

def screen_two():
    clear_frame()
    button_2 = tk.Button(window, text="Go to screen one", command=lambda: screen_one())
    button_2.pack(pady=10)
    label_2 = tk.Label(window, text="Label on window two")
    label_2.pack(pady=10)

def screen_one():
    clear_frame()
    button_1 = tk.Button(window, text="Go to screen two", command=lambda: screen_two())
    button_1.pack(pady=10)
    label_1 = tk.Label(window, text = "1")
    label_1.pack(pady=10, x = 300, y = 300)

window = tk.Tk()
window.title("Screen Switching Example")
window.geometry("1250x500")

screen_one()  # Show the initial screen
window.mainloop()