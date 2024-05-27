import enter

def main():
    enter.b.start()
    enter.b.manager = True
    e = enter.Enter()
    while True:
        enter.b.head()
        enter.b.bold()
        print("menu: ")
        print(" 1. acess to accounts")
        print(" 2. ban a username")
        print(" 3. recover the username")
        print(" 4. change a user's password")
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
            print("Recover a user")
            s = input("Here you can write the username you want: ")
            f = open('accounts/banned.txt', 'r')
            users = f.read().split('\n')
            f.close()
            f = open('accounts/banned.txt', 'w')
            for i in range(len(users)):
                if users[i] != s:
                    f.write(users[i] + '\n')
            print("press any key")
            enter.b.getch()
        if x == '4':
            mydict = enter.b.todict('accounts/users.json')
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

if __name__ == '__main__':
    main()