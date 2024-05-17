import basic as b

class Account:
    def __init__(self, username, isnew):
        self.name = username
        self.hname = b.hash(username)
        if isnew == True:
            self.create()
        self.show_dashboard()

    def create(self):
        b.os.mkdir('./accounts/' + self.hname)
        b.os.mkdir('./projects/' + self.hname)
        f = open('projects/projects_list.json', 'a')
        f.close()
        f = open('accounts/' + self.hname + '/invitations.txt', 'a')
        f.close()
        f = open('accounts/' + self.hname + '/message.txt', 'a')
        f.close()

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
        
        pass

    def show_messages(self):
        
        pass

    def show_invitations(self):
        
        pass
    
    def send_invatation(self):

        pass

    def show_projects(self):
        
        pass

    def create_projects(self):

        pass