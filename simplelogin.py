from tkinter import *
from functools import partial

def validateLogin(username, password):
    print("نام کاربری وارد شده:", username.get())
    print("رمز عبور وارد شده:", password.get())
    # در اینجا منطق تأیید اعتبار نام کاربری و رمز عبور را بنویسید

# ایجاد پنجره
tkWindow = Tk()
tkWindow.geometry('400x150')
tkWindow.title('فرم لاگین - pythonexamples.org')

# برچسب نام کاربری و جعبه متنی
usernameLabel = Label(tkWindow, text="نام کاربری").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)

# برچسب رمز عبور و جعبه متنی
passwordLabel = Label(tkWindow, text="رمز عبور").grid(row=1, column=0)
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)

# دکمه لاگین
validateLogin = partial(validateLogin, username, password)
loginButton = Button(tkWindow, text="ورود", command=validateLogin).grid(row=4, column=0)

tkWindow.mainloop()