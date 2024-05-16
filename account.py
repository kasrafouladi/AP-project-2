import basic as b

class Account:

    def __init__(self, username, backup):
        self.name = username
        self.hname = b.hash(username)
        if backup == True:
            self.create()
        else:
            self.back_up()
        self.show_dashboard()

    def create(self):
        pass

    def backup(self):
        pass

    def show_dashboard(self):
        b.head(self.name)

        pass

    def show_inbox(self, root):
        
        pass

    def show_invitations(self, root):
        
        pass
    
    def show_dashboard(self):

        pass

    def show_template(self, name, type):
        
        pass