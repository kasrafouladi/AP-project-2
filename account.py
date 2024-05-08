import json
import filecmp

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
    """
    user1 = username, user2 = hash(username)
    acess level: 1 = whatch(cant edit), 2 = can edit but just its own things, 3 = can do any thing(colider), 4 = 3 + can invite & kick out and its just owner
    """
    def __init__(self, user):
        self.user1 = user
        self.user2 = hash(user)
        
        # باز کردن فایل برای خواندن
        with open('./a.json', 'r') as f:
        # خواندن محتوای فایل
            file_contents = f.read()
        # چاپ محتوا
            print(file_contents)
        # فایل به طور خودکار بسته می‌شود

        return
    
a = Account("salam")
