import basic as b
'''
class Project:
    def __init__(self, name, p_addres, new):
        if new == True:
            self.create(name, p_addres)
        else:
            self.backup(name, p_addres)
        pass
    
    def create(self, name, p_addres):
        
        pass
'''    
    
def upload(s):
    file = open('table.txt', 'w')
    file.write(s)

def download():
    file = open('table.txt', 'r')
    return file.read()

def main():
    while True:
        b.head()
        upload("")
        cor = input().split()
        b.start_from(cor[0], cor[1])
        print('press a key to upload it into  system')
        b.getch()
        b.head()
        print('press a key to dowload it rom system')
        b.getch()
        b.head()
        s = download()
        print(s)
        
if __name__ == '__main__'
main()