import json
import simplelogin
import tkinter as tk

def hash(user):
    bs = [259, 258, 257, 256, 263]
    md = [1000000021, 1000000009, 1000000007, 998244353, 2000000011]
    res = ""

    for i in range(5):
        sum = 0
        for j in range(len(user)):
            sum = ((sum * bs[i]) + ord(user[j])) % md[i]
        s = str(sum)
        for j in range(11 - len(s)):
            res += '0'
        res += s

    return res

class Account:
    
    def __init__(self, user):
        self.user1 = user
        self.user2 = hash(user)
        
        with open('boards.json', 'r') as f:
            file_contents = f.read()
            self.boards = json.loads(file_contents)
        
        with open('inbox.json', 'r') as f:
            file_contents = f.read()
            self.inbox = json.loads(file_contents)
        return
    



def main():
    root = tk.Tk()
    root.mainloop()
    return

if __name__ == '__main__':
    main()