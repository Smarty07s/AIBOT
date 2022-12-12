import os

commit = input('Commit desc: ')
os.system('git add *')
os.system(f'git commit -m "{commit}"')
os.system('git push *')