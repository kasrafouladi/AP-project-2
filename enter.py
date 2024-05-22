import subprocess
import getpass
import basic as b
import account as acc

class Enter:
    def ent(self):
        sl = b.todict('accounts/saved_login.json')
        if b.time.time() - sl["time"] <= 7 * 24 * 60 * 60:
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
        print('-' * 120)
        print('IF you want to sign in write \'sign in\' in the form instead of username', end = '')
        b.bold(False)

        while True:
            b.start_from(7, 54)
            username = input()
            if username == 'sign in':
                self.signin()
                return
            password = b.getpsw(9, 54)
            confirmpassword = b.getpsw(11, 54)
            if self.validate_signup(username, password, confirmpassword) == 1:
                b.c_col(32)
                b.start_from(12, 0)
                print('Do you want to save your login for a week? (Y: yes/any other key: no) ', end = '', flush=True)
                b.c_col(37)
                c = b.getch()
                if c == 'Y':
                    b.tojson('accounts/saved_login.json', {"user": username, "time": b.time.time()})
                userslist = b.todict('accounts/users.json')
                userslist.update({username: b.hash(password)})
                b.tojson('accounts/users.json', userslist)
                acc.Account(username, True)
                return
            b.start_from(7, 54)
            print(' ' * len(username))
            b.start_from(9, 54)
            print(' ' * len(password))
            b.start_from(11, 54)
            print(' ' * len(confirmpassword))

    def validate_signup(self, username, password, confirmpassword):
        users = b.todict('accounts/users.json')
        b.c_col(31)
        ok = True
        if len(username) == 0:
            b.start_from(8, 54)
            print("Username's lenght can't be 0", end = "")
            ok = ok and False
        else:
            b.start_from(8, 54)
            print("                            ", end = "")

        if len(password) == 0:
            b.start_from(10, 54)
            print("Passwords's lenght can't be 0", end = "")
            ok = False
        else:
            b.start_from(10, 54)
            print("                             ", end = "")

        if username in users.keys():
            b.start_from(8, 54)
            print("This username is taken by another user", end = "")
            ok = False
        else:
            b.start_from(8, 54)
            print("                                      ", end = "")

        if password != confirmpassword:
            b.start_from(12, 54)
            print("Passwords aren't match", end = "")
            ok = False
        else:
            b.start_from(12, 54)
            print("                      ", end = "")
        
        return ok