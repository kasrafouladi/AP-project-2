import basic as b
import account as acc

class Enter:
    def ent(self):
        f = open('accounts/banned.txt', 'r')
        self.banned = f.read().split('\n')
        f.close()
        
        if b.manager == True:
            b.head()
            while True:
                b.user_handle = input("please enter the username: ")
                users = b.todict('accounts/users.json')
                if b.user_handle in users.keys():
                    acc.Account(b.user_handle, False)
                    return
                if len(b.user_handle) == 0:
                    return
                print("invalid username, try again or just press enter to back")
        
        sl = b.todict('accounts/saved_login.json')
        if b.time.time() - sl["time"] <= 7 * 24 * 60 * 60:
            b.user_handle = sl["user"]
            f = open("accounts/log.txt", "a")
            f.write("\n---------------\n")
            f.write(b.time.ctime() + "\n")
            f.write("SIGN IN - " + sl["user"] + " signed in\n")
            f.close()
            acc.Account(sl["user"], False)
        else:
            b.tojson('accounts/saved_login.json', {"user": "sign in", "time": 0})
            self.signin()

    def signin(self):
        b.head()
        b.start_from(5, 1)
        b.bold()
        print(' ' * 49 + 'Sign in')
        print(' ' * 40 + ' Username :\n')
        print(' ' * 40 + ' Password :\n')
        print('-' * 120)
        print('IF you want to sign in write \'sign up\' in the form instead of username', end = '')
        b.bold(False)

        while True:
            b.start_from(7, 54)
            username = input()
            if username == 'sign up':
                self.signup()
                return
            password = b.getpsw(9, 54)
            if self.validate_signin(username, password) == True:
                b.c_col(32)
                b.start_from(10, 5)
                print('Do you want to save your login for a week? (Y: yes/any other key: no) ', end = '', flush=True)
                b.c_col(37)
                c = b.getch()
                if c == 'Y':
                    b.tojson('accounts/saved_login.json', {"user": username, "time": b.time.time()})
                b.user_handle = username
                f = open("accounts/log.txt", "a")
                f.write("\n---------------\n")
                f.write(b.time.ctime() + "\n")
                f.write("SIGN IN - " + username + " signed in\n")
                if c == 'Y':
                    f.write("and saved the sign in for a week\n")
                f.close()
                acc.Account(username, False)
                return
            b.start_from(7, 54)
            print(' ' * len(username))
            b.start_from(9, 54)
            print(' ' * len(password))

    def validate_signin(self, username, password):
        users = b.todict('accounts/users.json')
        b.c_col(31)
        pasw = b.hash(password)
        b.start_from(10, 54)
        print('                               ', end = '')
        if username not in users.keys() or users[username] != pasw:
            b.start_from(10, 54)
            print('Username or password is invlaid', end = '')
            b.c_col(37)
            return 0
        if username in self.banned:
            b.start_from(10, 54)
            print('This username is banned', end = '')
            b.c_col(37)
            return 0
        b.c_col(37)
        return 1

    def signup(self):
        b.head()
        b.start_from(5, 1)
        b.bold()
        print(' ' * 49 + 'Sign up')
        print(' ' * 40 +' Username :\n')
        print(' '* 40 + ' Password :\n')
        print(' ' * 40 + ' Confirm :\n' + ' ' * 40  +'Password\n')
        print(' ' * 40  +'Email :\n')
        print('-' * 120)
        print('\n' + 'IF you want to sign in write \'sign in\' in the form instead of username', end = '')
        b.bold(False)

        while True:
            b.start_from(7, 54)
            username = input()
            if username == 'sign in':
                self.signin()
                return
            password = b.getpsw(9, 54)
            confirmpassword = b.getpsw(11, 54)
            
            b.start_from(14, 54)
            email = input()
            if email:
                email = email.lower()

            if self.validate_signup(username, password, confirmpassword, email) == 1:
                b.c_col(32)
                b.start_from(20, 0)
                print('Do you want to save your login for a week? (Y: yes/any other key: no) ', end = '', flush=True)
                b.c_col(37)
                c = b.getch()
                if c == 'Y':
                    b.tojson('accounts/saved_login.json', {"user": username, "time": b.time.time()})
                userslist = b.todict('accounts/users.json')
                userslist.update({username: b.hash(password)})
                b.tojson('accounts/users.json', userslist)

                emails = b.todict('accounts/emails.json')
                emails.update({username: email})
                b.tojson('accounts/emails.json', emails)

                b.user_handle = username
                f = open("accounts/log.txt", "a")
                f.write("\n---------------\n")
                f.write(b.time.ctime() + "\n")
                f.write("SIGN UP - " + username + " signed up\n")
                if c == 'Y':
                    f.write("and saved the sign in for a week\n")
                f.close()
                acc.Account(username, True)
                return
            
            # erase inputs in the from
            b.start_from(7, 54)
            print(' ' * len(username))
            b.start_from(9, 54)
            print(' ' * len(password))
            b.start_from(11, 54)
            print(' ' * len(confirmpassword))
            b.start_from(14, 54)
            print(' ' * len(email))

    def validate_signup(self, username, password, confirmpassword, email):
        users = b.todict('accounts/users.json')
        b.c_col(31)
        ok = True

        if len(username) == 0:
            b.start_from(8, 54)
            print("Username's length can't be 0          ", end = "")
            b.c_col(37)
            ok = False
        elif username == "sign up":
            b.start_from(8, 54)
            print("Username can't be sign up             ", end = "")
            ok = False
        elif username in users.keys():
            b.start_from(8, 54)
            print("This username is taken by another user", end = "")
            ok = False
        elif username in self.banned:
            b.start_from(8, 54)
            print("This username is banned               ", end = "")
            ok = False
        else:
            b.start_from(8, 54)
            print("                                      ", end = "")

        if len(password) == 0:
            b.start_from(10, 54)
            print("Password's length can't be 0", end = "")
            ok = False
        else:
            b.start_from(10, 54)
            print("                            ", end = "")

        if password != confirmpassword:
            b.start_from(12, 54)
            print("Passwords aren't match", end = "")
            ok = False
        else:
            b.start_from(12, 54)
            print("                      ", end = "")
        
        emails = b.todict('accounts/emails.json')

        if email == "":
            b.start_from(15, 54)
            print("Eneter an email     ", end = "")
            ok = False
        
        elif email in emails.values():
            b.start_from(15, 54)
            print("Email must be unique", end = "")
            ok = False
        else:
            b.start_from(15, 54)
            print("                    ", end = "")
        
        b.c_col(37)
        return ok