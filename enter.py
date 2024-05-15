import subprocess
import basic as b
#import account as acc

class Enter()
    def enter(self):
        sl = b.todict('accounts/saved_login.json')
        if b.time.time() - sl['time'] <= 7 * 24 * 60 * 60:
            acc.Enviorment.ac(sl['name'], backup=True)
        else:
            self.signin()

    def signin(self):
        b.head()
        b.start_from(8, 1)
        b.bold()
        print(' ' * 9 + 'Sign up')
        print('IF you want to sign in write \'sign up\' in the form instead of username', end = '')
        print('-' * 50)
        print('Username :\n')
        print('Password :\n')
        print('Confirm  :\nPassword\n')
        b.bold(False)

        while True:
            username = input()
            if(username == 'sign up')
                self.signin()
                return
            password

    def validate_sign_in(self, username, password):
        users = b.todict('accounts/users.json')
        return username in users.keys() and users[username] == password

    def signup(self):
        b.head()
        b.start_from(8, 1)
        b.bold()
        print(' ' * 9 + 'Sign in')
        print('IF you want to sign in write \'sign in\' in the form instead of username', end = '')
        print('-' * 50)
        print('Username :\n')
        print('Password :\n')
        print('Confirm  :\nPassword\n')
        b.bold(False)

        while True:
            username = input()
            if(username == 'sign in')
                self.signin()
                return
            password

    def validate_sign_up(self, username, password, confirmpassword):# 0:username and password can't be empty  -1: this username is taken by another account, -2: passwords aren't match
        users = b.todict('accounts/users.json')
        if len(username) == 0 or len(password) == 0:
            return 0
        if b.hash(username) in users.keys():
            return -1
        if password != confirmpassword:
            return -2
        return 1