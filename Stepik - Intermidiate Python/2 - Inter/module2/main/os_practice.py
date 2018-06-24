import os
import os.path

f = open('answers.txt', 'a')
for current_dir, dirs, files in os.walk("."):
    if list(filter(lambda x: x.endswith('.py'), files)):
        katalog = os.getcwd()
        f.write(katalog[-4:]+current_dir[1:]+'\n')




f.close()