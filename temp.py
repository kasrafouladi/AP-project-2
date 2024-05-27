import basic as b

class Task:
    def __init__(self, path):
        pass
        
    def show_history(self, path):
        f = open(path, 'r')
        b.head()
        b.bold()
        print("Here you can see the changes over this task:\n")
        b.bold(False)
        print(f.read())
        f.close()
        pass
        
    def update(self, name, added, deleted):
        pass
    
    def func():
        pass