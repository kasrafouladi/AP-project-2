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
        msg = Msg
        msg.send_message(msg, self.name)
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
        p.Project('projects/' + self.name + '/' + str(b.time.time()))
        pass
    
class Msg:
        
    def send_message(self, name):
        b.head()
        b.start_from(5, 5)
        print('From: ' + name, end = '')
        b.start_from(6, 5)
        print('To: ', end = '')
        b.start_from(7, 5)
        print('Subject: ', end = '')
        b.start_from(8, 1)
        print('_' * 50)
        b.start_from(6, 10)
        to = input()
        b.start_from(7, 15)
        subject = input()
        line = 9
        self.msg = ''
        while True:
            b.start_from(line, 5)
            c = b.getch()
            if ord(c) == 8:
                self.edit_message(self, line)
                line -= 1
            else:
                print(c, end = '')
            s = input()
            s = c + s
            self.msg += s + '\n'
            line += 1
    
    def edit_message(self, line):
        b.start_from(line, 1)
        s = 'enter the line withch you want to edit: '
        print(s)
        while True:
            try:
                b.start_from(line, len(s) + 2)
                eline = input()
                b.start_from(line, 0)
                print(' ' * (len(s) + 2 + len(eline)), end = '')
                b.start_from(int(eline) + 9, 5)
                break
            except ValueError:
                continue

    def show_messages(self):
        
        pass