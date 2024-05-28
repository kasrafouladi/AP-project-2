import basic as b
import account as a
import table

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
        f = open('projects/' + self.owner + '/' + self.id + '/name.txt', 'a')
        f.write(self.name)
        f.close()

        #make colab.json
        f = open('projects/' + self.owner + '/' + self.id + '/colab.json', 'a')
        f.write("{ }")
        f.close()

        #make log
        f = open('projects/' + self.owner + '/' + self.id + "/log.txt", "a")
        f.write("\n---------------\n")
        f.write(b.time.ctime() + "\n")
        f.write("Project created by " + self.owner + "\n")
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

        #colabs
        self.colabs = b.todict('projects/' + self.owner + '/' + self.id + '/colab.json')
        
        #table
        b.os.mkdir('projects/' + self.owner + '/' + self.id + '/table/')
        f = open('projects/' + self.owner + '/' + self.id + '/table/history.txt', 'a')
        f.close()
        
        f = open('projects/' + self.owner + '/' + self.id + '/table/table.txt', 'a')
        f.write('\tbacklog\ttodo\tdoing\tdone\tarchived\n')
        for i in range(1, 11):
            f.write(str(i) + '\t' * 4 + '\n')
        f.close()

        for i in range(1, 11):
            for j in range(1, 6):
                f = open('projects/' + self.owner + '/' + self.id + '/table/' + str(i) + '-' + str(j) + '.txt', 'a')
                f.close()
        #acc log
        f = open("accounts/" + self.owner + "/log.txt", "a")
        f.write("\n---------------\n")
        f.write(b.time.ctime() + "\n")
        f.write(self.owner + " created a project named " + self.name + "\n")
        f.close()

        print('Project created successfully!')
        print('Press any key to continue')
        b.getch()
        
    
    
    def project_menu(self):
        while True:
            b.head()
            b.bold()
            print("Projects name: " + self.name + ", Owner: " + self.owner)
            print("""
Project's Items:
  1. See Collaborators list
  2. Tasks Table
  3. Back
  4. Leave
  5. Kick Someone
  6. Show log
Enter a number: """)
            x = input()
            if x == '1':
                self.show_colabs()
            elif x == '2':
                self.show_table()
            elif x == '4': 
                del self.colabs[b.user_handle]
                b.tojson('projects/' + self.owner + '/' + self.id + '/colab.json', self.colabs)
                
                if b.manager == False:
                    f = open("projects/ " + self.owner + "/" + self.id + "/log.txt", "a")
                    f.write("\n---------------\n")
                    f.write(b.time.ctime() + "\n")
                    f.write(b.user_handle + " left the project" + "\n")
                    f.close()

                mydict = b.todict('projects/' + b.user_handle + '/projects_list.json')
                del mydict[self.name]
                b.tojson('projects/' + b.user_handle + '/projects_list.json', mydict)

                break
            elif x == '3':
                break
            elif x == '5':
                if b.user_handle != self.owner:
                    print("only owner can kicks someone")
                    b.getch()
                else:
                    b.bold(False)
                    handle = input("please enter the username of the collaborator: ")
                    if handle not in self.colabs.keys():
                        print("there is no such user in this project, press any key to continue")
                        b.getch()
                        continue

                    if b.manager == False:
                        f = open("projects/" + self.owner + "/" + self.id + "/log.txt", "a")
                        f.write("\n---------------\n")
                        f.write(b.time.ctime() + "\n")
                        f.write(self.owner + " kicked out " + handle + "\n")
                        f.close()

                    del self.colabs[handle]
                    b.tojson('projects/' + self.owner + '/' + self.id + '/colab.json', self.colabs)
                    mydict = b.todict('projects/' + handle + '/projects_list.json')
                    del mydict[self.name]
                    b.tojson('projects/' + handle + '/projects_list.json', mydict)
            elif x == '6':
                self.show_log()
        b.bold(False)        
    
    def show_colabs(self):
        b.head()
        print(self.name + "'s Collaborators:")
        for colab in self.colabs:
            print(" " + colab + ", Access level: " + str(self.colabs[colab][1]))
        print("press any key to continue")
        b.getch()
        
    def show_table(self):
        table.main_menu('projects/' + self.owner + '/' + self.id + '/table/', self.colabs[b.user_handle][1])

    def show_log(self):
        b.head()
        f = open("projects/" + self.owner + "/" + self.id + "/log.txt", "r")
        print(f.read())
        print("press any key to continue")
        b.getch()
        f.close()