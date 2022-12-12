import os



os.system('git set-url origin https://github.com/Smarty07s/AIBOT.git')
os.system('git add *')
commit = input('Commit desc: ')
os.system(f'git commit -m "{commit}"')
os.system('git push *')