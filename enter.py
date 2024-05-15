import subprocess
import basic as b

class LoginForm:
    def __init__(self):
        
        pass

    def validate_login(self, username, password):
        users = todict('accounts/users.json')
        return {username: password} in users
    
    def sign_up(self):
        RegistrationForm()


class RegistrationForm:
    def __init__(self):
        b.head()

    def validate_registration(username, password, confirmpassword):# 0:username and password can't be empty  -1: this username is taken by another account, -2: passwords aren't match
        users = todict('accounts/users.json')
        if len(username) == 0 or len(password) == 0:
            return 0
        if b.hash(username) in users.keys():
            return -1
        if password != confirmpassword:
            return -2
        return 1