#cd C:\Users\Lenovo\OneDrive\Desktop\AP-project-2

import subprocess
import os
os.system('cls')
# اجرای دستور زیر برای فعال‌سازی ANSI escape sequences
subprocess.run('', shell=True)

# تعیین مختصات کرسر در سطر چهارم و ستون دوم
print('enter password : ', end ='') 
print('\033[2;1H', end = "")
print('attempts: 0', end='')

cnt = 0

#how to find a file
#file = open('a/b.txt', 'r')
dc = {'salam': 1}
print("\033[5;30H", end = '')
print('salam' in dc.keys() and dc['salam'] == 1)
while True:
    print("\033[1;30H", end = '')
    x = input()
    print("\033[1;30H", end = '')
    print(' ' * len(x), end = '')
    print("\033[2;11H", end = '')
    cnt += 1
    print(cnt)