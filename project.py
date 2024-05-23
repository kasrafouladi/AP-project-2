import basic as b
import uuid
import json

class Project:
    def __init__(self, name, p_address, new, users, id=None, roles=None, leader=None, tasks=None):
        self.name = name
        self.p_address = p_address
        self.users = users
        self.id = id if id else str(uuid.uuid4())  
        self.roles = roles if roles else {}
        self.leader = leader
        self.tasks = tasks if tasks else []
        
        if new:
            self.create(name, p_address)
        else:
            self.backup(name, p_address)
    
    def create(self, name, p_address):
        b.head()
        b.bold()
        print('Create a new project')
        b.bold(False)
        name = input('Project name: ')
        address = 'projects/kasra/' + name
        leader = self.name
        id = str(uuid.uuid4())
        users = [self.name]
        roles = {self.name: 'leader'}
        tasks = []
        project = self.__init__(name, address, True, users, id, roles, leader, tasks)
        self.save()
        print('Project created successfully!')
        print('Press any key to continue')
        b.getch()
    
    def backup(self, name, p_address):
        pass
    
    def save(self):
        temp = self.name + '-' + self.id + '.json'
        address = self.p_address + temp 
        b.tojson(address, self.__dict__)
        
    def addTask(self, task):
        self.tasks.append(task)
        self.save()
    
    def addUser(self, user, role):
        self.users.append(user)
        self.roles[user] = role
        self.save()


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
