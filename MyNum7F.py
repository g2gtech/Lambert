"""
7. Write a recursive function that expects a pathname as an argument. The pathname can be either the name of a file or
the name of a directory. If the pathname refers to a file, its name is displayed, followed by its contents. Otherwise,
if the pathname refers directory, the function is applied to
each name in the directory. Test this function in a new program.

1. Significant constants:

2. The inputs are:

3. Computations:
    a. Determine if path is directory or file.
    b.
4. The outputs are new values for:
    a. If it is a file contents are displayed and if a directory those contents are displayed.
"""

import os.path
from os import listdir
from os.path import isfile, join

listdirs = []
listfiles = []

# filepath = 'C:\\Users\\Carlie\\Desktop'
# Receives input from the user for where the directory and files are located for evaluation.
# path_y = str(input("\nWhat is path where files or directories exists? <OR> Press \"Enter\" to EXIT: "))
path_y = 'C:\\Users\\Carlie\\Desktop'
filepath = path_y
if path_y == "":
    print("Bye!")
    exit()
print("\n\tYou are at path:\t\t", os.getcwd())
os.chdir(path_y)
print("\tPath being searched is: ", os.getcwd())
for root, dirnames, filenames in os.walk(os.getcwd()):
    for dirs in dirnames:
        path_x = os.path.join(root, dirs)
        listdirs.append(path_x)
        for files in filenames:
            path_file = os.path.join(path_x, files)
            listfiles.append(path_file)

print("\tNumber of directories\t", len(listdirs))
print("\tNumber of files\t\t\t", len(listfiles))
print("\tDone!\n")

print("isdir", os.path.isdir(filepath))
print("exists", os.path.exists(filepath))
print("chdir", os.chdir(filepath))
print("listdir", os.listdir(filepath))

filePath = 'C:\\Users\\Carlie\\Desktop\\Stuff'


def read(filePath):
    if os.path.exists(filePath):
        if os.path.isdir(filePath):
            # append path to list named listdirs
            listdirs.append(filePath)
            os.chdir(filePath)
            # 'e' is same as listdirs as list of directories
            e = os.listdir(filePath)
            # extracting elements in list 'e'
            for elements in e:
                # generates a path string with filename called 'path', from list 'e' with join command
                path = os.path.join(filePath, elements)
                print("e", path)
                read(path)
    else:
        if os.path.isfile(filePath):
            name = os.path.split(filePath)[1]
            # recursive operation
            print(name)
            content = ''
            with open(filePath, 'r') as file:
                for line in file:
                    content += line
                print(name + '\n-------------------------')
                print(content)
                print()

read(filePath)