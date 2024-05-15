import json
import os
import time
import subprocess
import msvcrt

def hash(s1):
    bs = [259, 258, 257, 256, 263]
    md = [1000000021, 1000000009, 1000000007, 998244353, 2000000011]
    res = ""
    for i in range(5):
        sum = 0
        for j in range(len(s1)):
            sum = ((sum * bs[i]) + ord(s1[j])) % md[i]
        s2 = str(sum)
        for j in range(11 - len(s2)):
            res += '0'
        res += s2
    return res

def todict(s):
    file = open(s, 'r')
    content = file.read()
    return json.loads(content)

def start():
    subprocess.run('', shell = True)

def head(user = ''):
    os.system('cls')
    bold()
    print('\033[33m', end = '')
    print('OC board')
    print('Created by: Orange Car')
    print('\033[37m', end = '')
    if len(user) != 0:
        print('_' * 50)
        print('\033[35m', end = '')
        print('~ ' + user)
        print('\033[37m', end = '')
    print('_' * 50)
    print('\033[32m', end = '')
    print('Local time: ' + time.ctime() + '\n')
    print('\033[37m', end = '')
    bold(False)

def start_from(x, y):
    s = '\033[' + str(x) + ';' + str(y) + 'H'
    print(s, end = '')

def bold(on = True):
    if on == True:
        print('\033[1m')
    else:
        print('\033[0m')

def getch():
    return msvcrt.getch().decode()

def main():
    start()
    head('kasra')
    start_from(10, 10)
    input()
    bold()
    print('Jableb')

if __name__ == '__main__':
    main()