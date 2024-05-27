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
    
    def create(self):
        b.os.mkdir('./accounts/' + self.name)
        b.os.mkdir('./projects/' + self.name)
        f = open('projects/' + self.name + '/projects_list.json', 'a')
        f.write("{ }")
        f.close()
        f = open('projects/' + self.name + '/my.json', 'a')
        f.write("{ }")
        f.close()
        f = open("accounts/" + self.name + "/log.txt", "a")
        f.write("\n")
        f.close()
        f = open('accounts/' + self.name + '/invitations.txt', 'a')
        f.close()
        f = open('accounts/' + self.name + '/message.txt', 'a')
        f.close()
        f = open('accounts/' + self.name + '/r_inv.txt', 'a')
        f.close()
        
    def show_menu(self):
        while True:
            b.head()
            b.bold()
            print("Menu: ")
            print(" 1. Send message")
            print(" 2. Show messages")
            print(" 3. Send invatation")
            print(" 4. Show invatations")
            print(" 5. Create a new project")
            print(" 6. Show projects")
            print(" 7. Owned projects")
            print(" 8. Sign out")
            print(" 9. Show log")
            print ('\n-------------------\nTo choose any item pleas enter its section number and press enter ', end = '')
            b.bold(False)
            s = b.getch()
            if s == '1':
                self.msg.send_message()
            if s == '2':
                self.msg.show_messages()
            if s == '3':
                self.inv.send_invitation()
            if s == '4':
                self.inv.show_invitation()
            if s == '5':
                self.create_project()
            if s == '6':
                self.show_projects()
            if s == '8':
                b.c_col(31)
                print("Are you sure you want to sign out? (Y: yes / any other key: no) ", end = '', flush=True)
                b.c_col(37)
                ch = b.getch()
                if ch != 'Y':
                    continue
                if b.manager == False:
                    f = open("accounts/log.txt", "a")
                    f.write("\n---------------\n")
                    f.write(b.time.ctime() + "\n")
                    f.write(self.name + " signed out\n")
                    f.close()
                b.tojson('accounts/saved_login.json', {"user" : "sign in", "time" : 0})
                b.user_handel = ""
                return
            if s == '7':
                self.show_my()

            if s == '9':
                b.head()
                f = open('accounts/' + self.name + '/log.txt', 'r')
                print(f.read())
                f.close()
                print("press any key to continue")
                b.getch()
            
    def show_my(self):
        b.head()
        b.bold()
        mydict = b.todict('projects/' + self.name + '/my.json')
        print("Here you can see the projects that you are the leader in them: ")
        for name in mydict:
            print("name: " + name + ", id: " + mydict[name])
        b.bold(False)
        print("press any key to continue")
        b.getch()

    def create_project(self):
        project = p.Project(owner = self.name, new = True)
        
    def show_projects(self):
        while True:
            projects = b.todict('projects/' + self.name + '/projects_list.json')
            names = [project for project in projects]
            b.head()
            b.bold()
            i = 1
            for project in projects:    
                print(' ' + str(i) + '. ' + project)
                i += 1
            print('-' * 50)
            print('To choose the project you want enter its crosspending number(to back into menu enter -1)')
            x = int(input())
            if x == -1:
                return
            p.Project(id = projects[names[x - 1]][0], owner = projects[names[x - 1]][2], name = names[x - 1], new = False)

######################################

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
        b.start_from(10, 2)
        print('Project id: ', end = '')
        b.bold(False)
        b.start_from(6, 10)
        to = input()
        b.start_from(7, 15)
        subject = input()
        self.msg = self.name + '\n' + to + '\n' + subject + '\n'
        b.start_from(9, 24)
        
        al = input()
        valid = ['2', '2', '3', '4']
        if al in valid:
            self.msg += al
        else:
            self.msg += '1'

        b.start_from(10, 24)
        id = input()
        self.msg += '\n' + id
        line = 11
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
            print('press a key to continue')
            ch = b.getch()
            return
        elif b.os.path.exists('projects/' + self.name + '/' + id + '/') == False:
            print('you are not the owner of this project')
            print('press a key to continue')
            ch = b.getch()
            return
        else:
            now = b.time.ctime()
            f = open('accounts/' + to + '/invitations.txt', 'a')
            f.write(now + '\n' + self.msg + "\n\n\n")
            f.close()
            f = open('accounts/' + to + '/r_inv.txt', 'a')
            f.write('N' + '\n')
            f.close()
            print('sent')
        print('press a key to continue')
        ch = b.getch()

    def show_invitation(self):
        while True:
            b.head()
            
            f = open('accounts/' + self.name + '/invitations.txt', 'r')
            s = f.read().split('\n\n\n')
            s = b.reverse(s)
            f.close()

            f = open('accounts/' + self.name + '/r_inv.txt', 'r')
            str1 = f.read().split('\n')
            str1 = b.reverse(str1)
            f.close()
            
            print("To read invitation you want pleas enter it's crosspending number:")
            str = [''] * len(s)
 
            for i in range(1, len(s)):
                str[i] = s[i].split('\n')
                if str1[i] == 'd':
                    b.c_col(31)
                elif str1[i] == 'a':
                    b.c_col(32)
                print(i,  end = '')
                print('. ', end = '')
                print(str[i][0], end = ', ')
                print(str[i][1], end = ', ')
                print(str[i][2])
                b.c_col(37)
            print('-------------------\nenter -1 to back into menu')
            
            n = int(input())
            if n == -1:
                return
            else:
                b.head()
                print('Time: ' + str[n][0])
                print('From: ' + str[n][1])
                print('Subject: ' + str[n][3])
                print('_' * 40)
                print(' Acess level: ' + str[n][4])
                for i in range(6, len(str[n])):
                    print(' ' + str[n][i])
                b.bold()
                print('----------\na: accept, d: decline, exit: e')
                if str1[n] == 'N':
                    ch = b.getch()
                    if ch != 'e':
                        if ch == 'a':
                            str1[n] = 'a'
                            #add to colab
                            mydict = b.todict('projects/' + str[n][1] + '/' + str[n][5] + '/colab.json')
                            mydict.update({self.name : [str[n][5], int(str[n][4])]})
                            b.tojson('projects/' + str[n][1] + '/' + str[n][5] + '/colab.json', mydict)
                    
                            f = open("accounts/" + self.name + "/log.txt", "a")
                            f.write("\n---------------\n")
                            f.write(b.time.ctime() + "\n")
                            f.write("Joined to the project with id: " + str[n][5] + "\n")
                            f.close()
                            #add to list
                            mydict = b.todict('projects/' + self.name + '/projects_list.json')
                            f = open('projects/' + str[n][1] + '/' + str[n][5] + '/name.txt', 'r')
                            mydict.update({f.read() : [str[n][5], int(str[n][4]), str[n][1]]})
                            f.close()
                            b.tojson('projects/' + self.name + '/projects_list.json', mydict)

                            f = open("projects/" + str[n][1] + '/' + str[n][5] + "/log.txt", "a")
                            f.write("\n---------------\n")
                            f.write(b.time.ctime() + "\n")
                            f.write(b.user_handle + " joined to the project" + "\n")
                            f.close()

                            print("accepted")

                        else:
                            str1[n] = 'd'
                            f = open("accounts/" + self.name + "/log.txt", "a")
                            f.write("\n---------------\n")
                            f.write(b.time.ctime() + "\n")
                            f.write("Declined invatation from the project with id: " + str[n][5] + "\n")
                            f.close()
                            print("declined")
                            

                elif str1[n] == 'a':
                    print("accepted")
                
                elif str1[n] == 'd':
                    print("declined")
                #update r_inv
                f = open('accounts/' + self.name + '/r_inv.txt', 'w')
                str1 = b.reverse(str1)
                for i in range(len(str1)):
                    if i != len(str1) - 1:
                        f.write(str1[i] + '\n')
                    else:
                        f.write(str1[i])
                f.close()

                b.bold(False)
                print('press any key to continue')
                b.getch()

#####################################################################3333
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
            b.head()
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
                b.head()
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
