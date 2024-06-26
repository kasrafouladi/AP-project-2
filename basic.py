import json
import os
import time
import subprocess
import msvcrt

user_handle = ""

admin_handle = ""

manager = False

def getpsw(x, y):
    bold()
    res = ''
    start_from(x, y)
    print(' ' * y)
    start_from(x, y)
    while True:
        c = getch()
        if ord(c) == 8:
            if len(res) > 0:
                res = res[:-1]
                start_from(x, y)
                print('\b \b', end = '', flush = True)
                y -= 1
            else:
                start_from(x, y)
                print(' ', end = '', flush = True)
        elif ord(c) == 13:
            bold(False)
            return res
        else:
            start_from(x, y)
            print('*', end = '', flush = True)
            y += 1
            res += c


def reverse(s):
    return s[::-1]


def todict(file_name):
    try:
        with open(file_name, "r") as json_file:
            my_dictionary = json.load(json_file)
        return my_dictionary
    except TypeError:
        return {}
    
    
def tojson(address, my_dict):
    json_file =  open(address, "w")
    json.dump(my_dict, json_file)


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


def start():
    subprocess.run('', shell = True)


def bold(on = True):
    if on == True:
        print('\033[1m')
    else:
        print('\033[0m')


def c_col(x):
    s = '\033[' + str(x) + 'm'
    print(s, end = '')


def getch():
    return msvcrt.getch().decode()


def head():
    os.system('cls')
    bold()
    c_col(33)
    print('OC board' + ' ' * 24  + 'Created by: Orange Car' + ' ' * 30, end = '')
    c_col(32)
    print('Local time: ' + time.ctime())
    c_col(35)
    if user_handle:
        if manager:
            print("~ " + admin_handle + " [" + user_handle + "]")
        else:
            print('~ ' + user_handle)
    elif manager:
        print('~ ' + admin_handle)
    c_col(37)
    print('_' * 120)
    bold(False)


def start_from(x, y):
    s = '\033[' + str(x) + ';' + str(y) + 'H'
    print(s, end = '')


def reverse(s):
    return s[::-1]