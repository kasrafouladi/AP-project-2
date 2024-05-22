import basic as b
#import project as p   

class Account:
    def __init__(self, username, isnew):
        self.name = username
        if isnew == True:
            self.create()
        else:
            self.backup()
        self.show_dashboard()

    def create(self):
        b.os.mkdir('./accounts/' + self.name)
        b.os.mkdir('./projects/' + self.name)
        f = open('projects/' + self.name + '/projects_list.json', 'a')
        f.close()
        f = open('accounts/' + self.name + '/invitations.txt', 'a')
        f.close()
        f = open('accounts/' + self.name + '/message.txt', 'a')
        f.close()

    def backup(self):
        pass

    def show_dashboard(self):
        b.head(self.name)
        msg = Msg()
        msg.show_messages(self.name)
        """
                    heading
        messages   invatations   projects
        1.......   1..........       
        2.......   2..........  
        3.......   3..........
        4.......   4..........
        5.......       .
        6.......       .
           .           .
           .       10..........
           .
        10......
        """
        pass

    def show_invitations(self):
        
        pass
    
    def send_invatation(self):

        pass

    def show_projects(self):
        # project -> name -> project list
        # entekhab
        # p = p.project(folan)
        # p.show()
        pass

    def create_projects(self):
        self.counter += 1            #name : [path, acess_level]
        self.projectlist.update({"board" + str(self.counter) : ['projects/' + self.name + '/' + str(b.time.time()), 4]})
        b.os.mkdir('projects/' + self.name + '/' + str(b.time.time()))
        #p.Project('projects/' + self.name + '/' + str(b.time.time()))
        pass
    
class Msg:
    def send_message(self, name):
        b.head()
        b.bold()
        b.start_from(5, 5)
        print('From: ' + name, end = '')
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
        self.msg = name + '\n' + to + '\n' + subject
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

    def show_messages(self, name):
        f = open('accounts/' + name + '/message.txt', 'r')
        s = f.read().split('\n\n\n')
        print(s)
        pass