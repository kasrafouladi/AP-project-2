import basic as b
import uuid
import json
import table
import account as a

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
        # temp things 
                # باز کردن فایل در حالت خواندن
        with open('projects/' + self.owner + '/' + self.id + '/' + self.name + ".txt", "r", encoding="utf-8") as file:
            # خواندن محتوای فایل
            self.table = file.read()
        self.colabs = b.todict('projects/' + self.owner + '/' + self.id + '/colab.json')
        # نمایش محتوای فایل
        print(table)
    

    def create(self):
        b.head()
        b.bold()
        print('Create a new project')
        b.bold(False)
        self.name = input('Project name: ')
        b.os.mkdir('projects/' + self.owner + '/' + self.id)
        #fill colab.json 
        project_colab_path = 'projects/' + self.owner + '/' + self.id + '/colab.json'
        f = open(project_colab_path, 'a')
        f.close()
        self.add_member(self.owner, 4)
        #fill user projcet list
        projects_list = b.todict('projects/' + self.owner + '/projects_list.json')
        projects_list.update({self.name: [self.id, 4, self.owner]})
        self.colabs = {self.owner: [self.id, 4]}
        b.tojson('projects/' + self.owner + '/' + self.id + '/colab.json', self.colabs)
        b.tojson('projects/' + self.owner + '/projects_list.json', projects_list)
        
        with open('projects/' + self.owner + '/' + self.id + '/' + self.name + ".txt", "w", encoding="utf-8") as file:
                file.write(table.tabulate(table.table_data, headers="firstrow", tablefmt='fancy_grid'))
        
        print('Project created successfully!')
        print('Press any key to continue')
        b.getch()
        
        
    def add_member(self, colabname, acess_level):
        with open('projects/' + self.owner + '/' + self.id + '/colab.json', 'r') as file:
            colab = b.todict(file)
            colab.update({colabname : acess_level})
            file.close()
            b.tojson('projects/' + self.owner + '/colab.json', colab)
    
    
    def project_menu(self):
        while True:
            b.head()
            b.bold()
            print("""
Project's Items:
  1. See Collaborators list
  2. Tasks Table
  3. Back
Enter a number: 
                  """)
            x = input()
            if x == '1':
                self.show_colabs()
            elif x == '2':
                table.main_menu('projects/' + self.owner + '/' + self.id + '/' + self.name + '.txt')
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
        
    def create_table():
        pass
    

class Task:
    def __init__(self, name, id, author, sdate, edate, priority, status):
        self.name = name
        self.id = id
        self.author = author
        self.sdate = sdate
        self.edate = edate
        self.priority = priority
        self.status = status
        
        self.comments = []
        self.assignees = []
        self.history = []

    def setStartDate(self, sdate):
        self.addToHistory()
        self.sdate = sdate

    def addToHistory(self):
        self.history.append({
            'name': self.name,
            'id': self.id,
            'author': self.author,
            'sdate': self.sdate,
            'edate': self.edate,
            'priority': self.priority,
            'status': self.status,
            'comments': self.comments[:],
            'assignees': self.assignees[:]
        })

    def addComment(self, comment):
        self.addToHistory()
        self.comments.append(comment)

    def assignUser(self, user):
        self.assignees.append(user)
        self.addToHistory()


class Comment:
    def __init__(self, author, date, message):
        self.author = author
        self.date = date
        self.message = message


################################################################################################
