import basic as b
import project as p

class Account:
    def __init__(self, username, isnew):
        self.name = username
        self.msg = Msg(username)
        self.inv = Invite(username)
        if isnew == True:
            self.create()
        self.show_menu()
    
        
    def show_menu(self):
        while True:
            b.head(self.name)
            b.bold()
            print("Menu: ")
            print(" 1. Send message")
            print(" 2. Show messages")
            print(" 3. Send invatation")
            print(" 4. Show invatations")
            print(" 5. Create a new project")
            print(" 6. Show projects")
            print(" 7. Sign out")
            print ('\n-------------------\nTo choose any item pleas enter its section number and press enter ', end = '')
            b.bold(False)
            s = b.getch()
            if s == '1':
                self.msg.send_message(self.name)
            if s == '2':
                self.msg.show_messages(self.name)
            if s == '3':
                self.inv.send_invitation(self.name)
            if s == '4':
                self.inv.show_invitation()
            if s == '5':
                self.create_project()
            if s == '7':
                b.c_col(31)
                print("Are you sure you want to sign out? (Y: yes / any other key: no) ", end = '', flush=True)
                b.c_col(37)
                ch = b.getch()
                if ch != 'Y':
                    continue
                b.tojson('accounts/saved_login.json', {"user" : "sign in", "time" : 0})
                return
            
    def createe_project(self):
        project = p(self.name, "", True, [self.name], roles={self.name: 'leader'}, leader=self.name)
        project.create(self.name, "")
        
class Msg:
    def __init__(self, name):
        self.name = name

    def send_message(self):
        b.head()
        b.bold()
        b.start_from(5, 5)
        print('From: ' + self.name, end = '')
        b.start_from(6, 5)
        print('To: ', end = '')
        b.start_from(7, 5)
        print('Subject: ', end = '')
        b.start_from(8, 1)
        print('_' * 50)
        b.start_from(18, 1)
        print('-------------------------\nHere you can send messages to any one you want to send it press enter twice', end = '')
        b.bold(False)
        b.start_from(6, 10)
        to = input()
        b.start_from(7, 15)
        subject = input()
        self.msg = self.name + '\n' + to + '\n' + subject
        line = 9
        while line < 18:
            b.start_from(line, 2)
            s = input()
            line += 1
            if len(s) == 0:
                break
            self.msg += '\n' + s
        b.start_from(20, 1)
        b.bold()
        print('Press any key to send this message ', end = '')
        b.bold(False)
        ch = b.getch()
        if b.os.path.exists('accounts/' + to + '/') == False:
            print('there is no such user')
            return
        else:
            now = b.time.ctime()
            f = open('accounts/' + to + '/message.txt', 'a')
            f.write(now + '\n' + self.msg + "\n\n\n")
            f.close()
            print('sent')
        print('press a key to continue')
        ch = b.getch()

    def show_messages(self):
        while True:
            f = open('accounts/' + self.name + '/message.txt', 'r')
            s = f.read().split('\n\n\n')
            s = b.reverse(s)
            b.head(self.name)
            print("To read message you want pleas enter it's crosspending number:")
            str = [''] * len(s)
            for i in range(1, len(s)):
                str[i] = s[i].split('\n')
                print(i,  end = '')
                print('. ', end = '')
                print(str[i][0], end = ', ')
                print(str[i][1], end = ', ')
                print(str[i][2])
            print('-------------------\nenter -1 to back into menu')
            n = int(input())
            if n == -1:
                return
            else:
                b.head(self.name)
                print('Time: ' + str[n][0])
                print('From: ' + str[n][1])
                print('Subject: ' + str[n][3])
                print('_' * 40)
                for i in range(4, len(str[n])):
                    print(' ' + str[n][i])
                b.bold()
                print('----------\npress a key to continue')
                ch = b.getch()
                b.bold(False)

class Invite:
    def __init__(self, name):
        self.name = name

    def send_invitation(self):
        b.head()
        b.bold()
        b.start_from(5, 5)
        print('From: ' + self.name, end = '')
        b.start_from(6, 5)
        print('To: ', end = '')
        b.start_from(7, 5)
        print('Subject: ', end = '')
        b.start_from(8, 1)
        print('_' * 50)
        b.start_from(18, 1)
        print('-------------------------\nHere you can write description if you want if you dont want just press enter twice', end = '')
        b.start_from(9, 2)
        print('Acess level(1/2/3/4): ', end = '')
        b.bold(False)
        b.start_from(6, 10)
        to = input()
        b.start_from(7, 15)
        subject = input()
        self.msg = self.name + '\n' + to + '\n' + subject + '\n'
        b.start_from(9, 24)
        al = input()
        self.msg += 'Acess level: ' + al
        line = 10
        while line < 18:
            b.start_from(line, 2)
            s = input()
            line += 1
            if len(s) == 0:
                break
            self.msg += '\n' + s
        b.start_from(20, 1)
        b.bold()
        print('Press any key to send this message ', end = '')
        b.bold(False)
        ch = b.getch()
        if b.os.path.exists('accounts/' + to + '/') == False:
            print('there is no such user')
            return
        else:
            now = b.time.ctime()
            f = open('accounts/' + to + '/invitations.txt', 'a')
            f.write(now + '\n' + self.msg + "\n\n\n")
            f.close()
            print('sent')
        print('press a key to continue')
        ch = b.getch()

    def show_invitation(self):
        while True:
            f = open('accounts/' + self.name + '/invitations.txt', 'r')
            s = f.read().split('\n\n\n')
            s = b.reverse(s)
            b.head(self.name)
            print("To read invitation you want pleas enter it's crosspending number:")
            str = [''] * len(s)
            for i in range(1, len(s)):
                str[i] = s[i].split('\n')
                print(i,  end = '')
                print('. ', end = '')
                print(str[i][0], end = ', ')
                print(str[i][1], end = ', ')
                print(str[i][2])
            print('-------------------\nenter -1 to back into menu')
            n = int(input())
            if n == -1:
                return
            else:
                b.head(self.name)
                print('Time: ' + str[n][0])
                print('From: ' + str[n][1])
                print('Project Name: ' + str[n][3])
                print('_' * 40)
                for i in range(4, len(str[n])):
                    print(' ' + str[n][i])
                b.bold()
                print('----------\na: accept, d: decline, exit: e')
                ch = b.getch()
                if ch != 'e':
                    if ch == 'a':
                        pass
                    else:
                        pass
                b.bold(False)