import account as ac

def clear_frame(root):        
    for widget in root.winfo_children():
        widget.destroy()
    return

class LoginForm:
    def __init__(self, root):
        self.root = root
        self.root.title('Enter')

        self.head_label = ac.bo.tk.Label(self.root, text = 'Login', font = ('calibri', 14))
        self.head_label.grid(row = 0, column = 1)

        self.username_label = ac.bo.tk.Label(self.root, text = 'Username')
        self.username_label.grid(row = 1, column = 0)
        self.username = ac.bo.tk.StringVar()
        self.username_entry = ac.bo.tk.Entry(self.root, textvariable=self.username)
        self.username_entry.grid(row = 1, column = 1)

        self.s = ac.bo.tk.Label(self.root, text = '')
        self.s.grid(row = 2, column = 1)

        self.password_label = ac.bo.tk.Label(self.root, text = 'Password')
        self.password_label.grid(row = 3, column = 0)
        self.password = ac.bo.tk.StringVar()
        self.password_entry = ac.bo.tk.Entry(self.root, textvariable=self.password, show = '*')
        self.password_entry.grid(row = 3, column = 1)

        self.isok = ac.bo.tk.Label(self.root, text = '')
        self.isok.grid(row = 4, column = 1)

        self.saved_login = ac.bo.tk.StringVar()
        self.checkmark = ac.bo.ttk.Checkbutton(self.root, text= 'Remember me', variable= self.saved_login, onvalue = '1', offvalue = '0')
        self.checkmark.grid(row = 5, column = 1)

        self.register_button = ac.bo.tk.Button(self.root, text = 'Login', command= self.validate_login)
        self.register_button.grid(row = 6, column = 0)
        self.exit_button = ac.bo.tk.Button(self.root, text = 'Create account', command=self.ext)
        self.exit_button.grid(row = 6, column = 1)
        return

    def ext(self):
        clear_frame(self.root)
        RegistrationForm(self.root)
        return

    def validate_login(self):
        self.isok.config(text = '')
        #edame
        return

class RegistrationForm:
    def __init__(self, root):
        self.root = root
        self.root.title('Registration')

        self.head_label = ac.bo.tk.Label(self.root, text = 'Register', font = ('calibri', 14))
        self.head_label.grid(row = 0, column = 1)

        self.username_label = ac.bo.tk.Label(self.root, text = 'Username')
        self.username_label.grid(row = 1, column = 0)
        self.username = ac.bo.tk.StringVar()
        self.username_entry = ac.bo.tk.Entry(self.root, textvariable=self.username)
        self.username_entry.grid(row = 1, column = 1)
        
        self.username_sub_label = ac.bo.tk.Label(self.root, text = '')
        self.username_sub_label.grid(row = 2, column = 1)         

        self.password_label = ac.bo.tk.Label(self.root, text = 'Password')
        self.password_label.grid(row = 3, column = 0)
        self.password = ac.bo.tk.StringVar()
        self.password_entry = ac.bo.tk.Entry(self.root, textvariable = self.password, show = '*')
        self.password_entry.grid(row = 3, column = 1)
        
        self.password_sub_label = ac.bo.tk.Label(self.root, text = '')
        self.password_sub_label.grid(row = 4, column = 1)

        self.confirm_password_label = ac.bo.tk.Label(self.root, text = 'Confirm\nPassword')
        self.confirm_password_label.grid(row = 5, column = 0)
        self.confirm_password = ac.bo.tk.StringVar()
        self.confirm_password_entry = ac.bo.tk.Entry(self.root, textvariable = self.confirm_password, show = '*')
        self.confirm_password_entry.grid(row = 5, column = 1)
        
        self.confirm_password_sub_label = ac.bo.tk.Label(self.root, text = '')
        self.confirm_password_sub_label.grid(row = 6, column = 1)

        self.saved_login = ac.bo.tk.StringVar()
        self.checkmark = ac.bo.ttk.Checkbutton(self.root, text = 'Remember me', variable= self.saved_login, onvalue = '1', offvalue = '0')
        self.checkmark.grid(row = 7, column = 1)

        self.register_button = ac.bo.tk.Button(self.root, text = 'Regirster', command=self.validate_registration)
        self.register_button.grid(row = 8, column = 0)
        self.exit_button = ac.bo.tk.Button(self.root, text = 'Have an account', command=self.ext)
        self.exit_button.grid(row = 8, column = 1)
        return

    def ext(self):
        clear_frame(self.root)
        LoginForm(self.root)
        return

    def validate_registration(self):
        self.username_sub_label.config(text = '')
        self.password_sub_label.config(text = '')
        self.confirm_password_sub_label.config(text = '')

        user = self.username.get()
        pasw = self.password.get()
        conf = self.confirm_password.get()
        isok = [True, True]

        if len(user) < 2:
            self.username_sub_label.config(text='username\'s length has\nto be between 2-20')
            return

        for c in user:
            isok[0] = (ord('a') <= ord(c) <= ord('z')) or (ord('A') <= ord(c) <= ord('Z')) or (ord('0') <= ord(c) <= ord('_'))
            if not isok[0]:
                break
        if not isok[0]:
            self.username_sub_label.config(text='usernames\'s characters\n have to be English\n alphabet or numbers or _')
            return

        for c in pasw:
            isok[1] = (ord('a') <= ord(c) <= ord('z')) or (ord('A') <= ord(c) <= ord('Z')) or (ord('0') <= ord(c) <= ord('_'))
            if not isok[1]:
                break
        if not isok[1]:
            self.password_sub_label.config(text='password\'s characters\n have to be English\n alphabet or numbers or _')
            return

        if len(pasw) < 8:
            self.password_sub_label.config(text='password\'s length has to be more or equal to 8')
            return
        if pasw != conf:
            self.confirm_password_sub_label.config(text='password isn\'t match')
            return
        return

def enter(root):
    if ac.bo.check_internet_connection():
        with open('saved_login.json', 'r') as f:
            file_contents = f.read()
            dict = ac.bo.json.loads(file_contents)
            if ac.bo.time.time() - dict["time"] <= 7 * 24 * 60 * 60:
                dict["time"] = ac.bo.time.time()
                a = ac.account.Account(dict["name"])
                a.update_files()
                a.show_dashboard(root)
            else:
                dict["time"] = 0
                dict["user"] = ""
                with open('saved_login.json','w') as outfile:
                    ac.bo.json.dump(dict, outfile)
                LoginForm(root)
    #else:

    #if a saved login existed enter, otherwise continue

    #badesh ke ok shod injoori pish boro
                              #/saved login bood bala biare            
            # age online nabood)
                              #\saved login nabood kari nakone o bege shoma online nistin
        
                            #/saved login bood update kone age conflict bood behesh bege va male server olaviate
            # age online bood)
                            #\saved login nabood ham bere file hashoo download kone
    return