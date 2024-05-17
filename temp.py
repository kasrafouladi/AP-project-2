import os

class Section:
    def __init__(self, history_address):
        self.history_address = history_address
        
    def show_history(self):
        os.system('cls')  
        with open(self.history_address, 'r') as file:
            mohtava = file.read()
            print(mohtava)
        
    def update(self, name, added, deleted):
        with open(self.history_address, 'a') as file:
            file.write("User: " + name + '\n')
            file.write('+' + added + '\n')
            file.write('-' + deleted + '\n')
            file.write("-----------------------\n")

class Temp:
    def __init__(self, name):
        self.name = name
        self.sec_list = [Section('histo.txt') for _ in range(100)]
    
    def get_name(self):
        return self.name

tmp = Temp("hamta")

added = input("Enter added content: ")
deleted = input("Enter deleted content: ")
name = input("Write your name: ")

tmp.sec_list[0].update(name, added, deleted)

tmp.sec_list[0].show_history()
