import basic as b
import account as a
import temp

class Project:
    def __init__(self, id = "", owner = "", new = False, name = ""):
        self.owner = owner
        if new:
            self.id = id if id else str(int(b.time.time()))
            self.create()
            
        else:
            self.backup(name, id)
        self.project_menu()

    def backup(self, name, id):
        self.name = name
        self.id = id
        self.colabs = b.todict('projects/' + self.owner + '/' + self.id + '/colab.json')
        pass   

    def create(self):
        b.head()
        b.bold()
        print('Create a new project')
        b.bold(False)
        self.name = input('Project name: ')
        b.os.mkdir('projects/' + self.owner + '/' + self.id)
        #make name
        f = open('projects/' + self.owner + '/' + self.id + '/name.json', 'a')
        f.write(self.name)
        f.close()

        #make colab.json
        f = open('projects/' + self.owner + '/' + self.id + '/colab.json', 'a')
        f.write("{ }")
        f.close()

        mydict = b.todict('projects/' + self.owner + '/' + self.id + '/colab.json')
        mydict.update({self.owner : [self.id, 5]})
        b.tojson('projects/' + self.owner + '/' + self.id + '/colab.json', mydict)
        
        #upd projects_list
        mydict = b.todict('projects/' + self.owner + '/projects_list.json')
        mydict.update({self.name : [self.id, 5, self.owner]})
        b.tojson('projects/' + self.owner + '/projects_list.json', mydict)

        #upd my projcets
        mydict = b.todict('projects/' + self.owner + '/my.json')
        mydict.update({self.name : self.id})
        b.tojson('projects/' + self.owner + '/my.json', mydict)

        #somthing
        self.colabs = b.todict('projects/' + self.owner + '/' + self.id + '/colab.json')
        
        print('Project created successfully!')
        print('Press any key to continue')
        b.getch()
        
    
    
    def project_menu(self):
        while True:
            b.head()
            b.bold()
            print("Projects name" + self.name + ", Owner: " + self.owner)
            print("""
Project's Items:
  1. See Collaborators list
  2. Tasks Table
  3. Back
Enter a number: """)
            x = input()
            if x == '1':
                self.show_colabs()
            elif x == '2':
                self.show_table()
            elif x == '3':
                break
        b.bold(False)        
    
    def show_colabs(self):
        b.head()
        print(self.name + "'s Collaborators:")
        for colab in self.colabs:
            print(" " + colab + ", Access level: " + str(self.colabs[colab][1]))
        print("press any key to continue")
        b.getch()
        
    def show_table():
        pass