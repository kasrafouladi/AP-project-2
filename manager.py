import enter
import argparse

class Manager:
    def __init__(self):
        enter.b.start()
        enter.b.manager = True
        parser = argparse.ArgumentParser(description="applications manager")
        subparsers = parser.add_subparsers(title="arguments", dest="command")

        # create-admin
        create_admin_parser = subparsers.add_parser("create-admin", help = "creates an admin")
        create_admin_parser.add_argument("--username", required=True, help = "admins user name")
        create_admin_parser.add_argument("--password", required=True, help = "admins password")

        # enter-admin
        enter_admin_parser = subparsers.add_parser("enter-admin", help = "let you enter as admin")
        enter_admin_parser.add_argument("--username", required=True, help = "admins user name")
        enter_admin_parser.add_argument("--password", required=True, help = "admins password")
        
        # reset
        reset_parser = subparsers.add_parser("purge-data", help = "resets any thing")

        args = parser.parse_args()

        if args.command == "create-admin":
            self.create(args.username, args.password)
        if args.command == "enter-admin":
            self.enter(args.username, args.password)
        elif args.command == "purge-data":
            self.reset()
    
    def enter(self, username, password):
        mydict = enter.b.todict("managers/admins.json")
        if username not in mydict.keys() or enter.b.hash(password) != mydict[username]:
            print("Invalid username or password")
            return
        enter.b.admin_handle = username
        self.menu()
    
    def create(self, username, password):
        mydict = enter.b.todict("managers/admins.json")
        if username in mydict.keys():
            print("This username is taken by another admin")
            return
        else:
            mydict.update({username: enter.b.hash(password)})
            enter.b.tojson("managers/admins.json", mydict)
            enter.b.admin_handle = username
            print("New admin created! press any key to continue")
            enter.b.getch()
        self.menu()

    def menu(self):
        e = enter.Enter()
        while True:
            enter.b.head()
            enter.b.bold()
            print("Menu: ")
            print(" 1. acess to accounts")
            print(" 2. ban a username")
            print(" 3. recover the username")
            print(" 4. change a user's password")
            print(" 5. exit")
            print(" 6. reset facotry")
            print(" 7. show log")
            print(" 8. accounts list")
            enter.b.bold(False)
            x = input()

            if x == '1':
                e.ent()
            
            if x == '2':
                enter.b.head()
                print("Ban a user")
                s = input("Here you can write the username you want: ")
                
                if s not in enter.b.todict('accounts/users.json').keys():
                    print("no such user press any key to countinue")
                    enter.b.getch()
                
                f = open('accounts/banned.txt', 'a')
                f.write(s + '\n')
                f.close()
                if enter.b.todict('accounts/saved_login.json')["user"] == s:
                    f = open("accounts/saved_login.json", "a")
                    f.write("{\"user\": \"sign in\", \"time\": 0}")
                    f.close()
                
                print("user banned press any key to countinue")
                enter.b.getch()
            
            if x == '3':
                enter.b.head()

                print("Recover a user\n")
                f = open('accounts/banned.txt', 'r')
                users = f.read().split('\n')
                f.close()

                print("Banned users:")
            
                for i in range(len(users)):
                    print(users[i])
            
                s = input("--------------\nHere you can write the username you want(or just press enter): ")

                f = open('accounts/banned.txt', 'w')
                for i in range(len(users)):
                    if users[i] != s:
                        f.write(users[i] + '\n')
                f.close()

                if s in users:
                    print("user recovered successfully")
                else:
                    print("invalid username")

                print("press any key")
                enter.b.getch()
            
            if x == '4':
                mydict = enter.b.todict('accounts/users.json')
                enter.b.head()
                print("Change pass word")
                user = input("user name: ")
                if user not in mydict.keys():
                    print("invalid username")
                else:
                    pasw = input("new pass word: ")
                    mydict[user] = enter.b.hash(pasw)
                    enter.b.tojson('accounts/users.json', mydict)
                print("press any key")
                enter.b.getch()
            
            if x == '5':
                print('Exitting..')
                break

            if x == '6':
                self.reset()
            
            if x == '7':
                enter.b.head()
                f = open("accounts/log.txt", "r")
                s = f.read()
                print("Here you can see log:\n" + s)
                f.close()
                print("press any key to continue")
                enter.b.getch()

            if x == '8':
                users = enter.b.todict("accounts/users.json")
                enter.b.head()
                print("Accounts: \n")
                for name in users.keys():
                    print(name)
            
                print("--------\npress a key")
                enter.b.getch()
    
    def reset(slef):
        enter.b.c_col(31)
        print("Do you really want to reset any thing? (Y: yes/any other key: no)")
        enter.b.c_col(37)
        c = enter.b.getch()
        if c != 'Y':
            return
          
        import shutil

        shutil.rmtree('accounts/')
        shutil.rmtree('projects/')
        enter.b.os.mkdir('accounts')
        enter.b.os.mkdir('projects')

        f = open("accounts/banned.txt", "a")
        f.write("\n")
        f.close()
            
        f = open("accounts/log.txt", "a")
        f.write("\n")
        f.close()
            
        f = open("accounts/users.json", "a")
        f.write("{ }")
        f.close()

        f = open("accounts/emails.json", "a")
        f.write("{ }")
        f.close()

        f = open("accounts/saved_login.json", "a")
        f.write("{\"user\": \"sign in\", \"time\": 0}")
        f.close()


if __name__ == '__main__':
    m = Manager()
