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

    def send_message(self):
        b.head()
        print('From: ' + self.name)
        print('To: ')
        print('Subject: ')
        print('_' * 50)
        b.start_from()
        pass

    def show_messages(self):
        
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
    