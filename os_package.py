# ******--    os package 

# ----------- few important functions related to builtin os package 

import os

# print(dir(os))      # prints files and directories in current directory

# print(os.getcwd())  # prints current working directory location

# os.chdir('pythonTuto')  # change to pythonTuto directory

# print(os.listdir())     # lists current directory's files and directories

# os.mkdir('sdfs')        # create dir

# os.rmdir('sdfs')        # delete dir

# os.rename('adobe','probe')  # changes directory name 'adobe' directory to 'probe' 

# prints all filename, directories and path from the 'e:\python'
# for path, dir, file in os.walk('e:\python'):
#     print(path)
#     print(dir)
#     print(file)

# print(os.getlogin())    # print currently logged in account name

print(os.name)    # retrieves information identifying the true operating system you are running on
