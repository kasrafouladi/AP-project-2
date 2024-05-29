import enter

def main():
    enter.b.start()
    enter.b.manager = True
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
            f = open('accounts/banned.txt', 'a')
            enter.b.head()
            print("Ban a user")
            s = input("Here you can write the username you want: ")
            f.write(s + '\n')
            f.close()
            print("press any key")
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
            enter.b.c_col(31)
            print("Do you really want to reset any thing? (Y: yes/any other key: no)")
            enter.b.c_col(37)
            c = enter.b.getch()
            if c != 'Y':
                continue
            
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

            f = open("accounts/saved_login.json", "a")
            f.write("{\"user\": \"sign in\", \"time\": 0}")
            f.close()
            
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
        
if __name__ == '__main__':
    main()