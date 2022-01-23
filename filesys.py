"""
CIAT Class:  ASD210 Fundamentals of Python - First Programs
STUDENT: Felicito A. Rustique
INSTRUCTOR: Nathan Kilgore
ASSIGNMENT: Week3 Part1 Exercise #1 
File: filesys.py  
Project 6.6
Provides a menu-driven tool for navigating a file system
and gathering information on files. Adds a command to view a file's contents.
"""

import os, os.path

QUIT = '8'

COMMANDS = ('1', '2', '3', '4', '5', '6', '7', '8')

MENU = """1   View files in current directory  
2   Move up one directory
3   Move down one directory
4   Number of files/folders in current directory
5   Size of the current directory in bytes
6   Search for a file name
7   View contents of a file
8   Quit the program"""

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def main():
    clearConsole()
    while True:
        print("PYTHON FILE SYSTEM MENU\n")
        print(MENU)
        print(f"\nCurrent directory: {(os.getcwd())}")
        command = acceptCommand()
        runCommand(command)
        if command == QUIT:
            print("Have a nice day!")
            break

def acceptCommand():
    """Inputs and returns a legitimate command number."""
    while True:
        command = input(f"\nEnter menu number: ")
        if not command in COMMANDS:
            print("Error: command not recognized")
        else:
            return command

def runCommand(command):
    """Selects and runs a command."""
    #if command == '1':
    #    print(f"Current directory: {(os.getcwd())}\n")
        #listCurrentDir(os.getcwd())
    if command == '1':
        viewFiles(os.getcwd())
    elif command == '2':
        moveUp()
    elif command == '3':
        moveDown(os.getcwd())
    elif command == '4':
        numFiles = countFiles(os.getcwd())
        print(f"The total number of files/folders is: {numFiles}\n")
    elif command == '5':
        numBytes = countBytes(os.getcwd())
        print(f"The total number of bytes is: {numBytes}\n")
    elif command == '6':
        target = input("Enter the search string: ")
        fileList = findFiles(target, os.getcwd())
        if not fileList:
            print("String not found\n")
        else:
            print("\nResults: ")
            for f in fileList:
                print(f)
            print()
    elif command == '7':
        viewContents(os.getcwd())

#MENU #1: VIEW FILES IN CURRENT DIRECTORY    
def viewFiles(dirName):
    """Prints a list of the cwd's contents."""
    print()
    lyst = os.listdir(dirName)
    for element in lyst: print(element)
    print()

#MENU #2: MOVE UP
def moveUp():
    """Moves up to the parent directory."""
    os.chdir("..")
    print("\nDirectory changed.")
    
#MENU #3: MOVE DOWN
def moveDown(currentDir):
    """Moves down to the named subdirectory if it exists."""
    print("Subdirectories in your current location: \n")
    lyst = os.listdir(currentDir)
    for element in lyst:
        if not os.path.isfile(element):
            print(element)
    newDir = input("\nEnter subdirectory to move down to: ")    
    if os.path.exists(currentDir + os.sep + newDir) and \
       os.path.isdir(newDir):
        os.chdir(newDir)
        print(f"Current directory: {(os.getcwd())}\n")
    else:
        print("ERROR: no such name\n")
        
#MENU #4: NUMBER OF FILES IN THE DIRECTORY
def countFiles(path):
    """Returns the number of files in the cwd and
    all its subdirectories."""
    count = 0
    lyst = os.listdir(path)
    for element in lyst:
        if os.path.isfile(element):
            count += 1
        #NOT INTERESTED IN COUNTING FILES IN SUBDIRECTORIES:
        #else:
        #    os.chdir(element)
        #    count += countFiles(os.getcwd())
        #    os.chdir("..")
    return count

#MENU #5: SIZE OF THE DIRECTORY IN BYTES
def countBytes(path):
    """Returns the number of bytes in the cwd and
    all its subdirectories."""
    count = 0
    lyst = os.listdir(path)
    for element in lyst:
        if os.path.isfile(element):
            count += os.path.getsize(element)
        else:
            os.chdir(element)
            count += countBytes(os.getcwd())
            os.chdir("..")
    return count

#MENU #6: SEARCH FOR A FILE NAME
def findFiles(target, path):
    """Returns a list of the file names that contain
    the target string in the cwd and all its subdirectories."""
    files = []
    lyst = os.listdir(path)
    for element in lyst:
        if os.path.isfile(element):
            if target in element:
                #files.append(path + os.sep + element)
                files.append(element)
        else:
            os.chdir(element)
            files.extend(findFiles(target, os.getcwd()))
            os.chdir("..")
    return files

#MENU #7: VIEW CONTENTS OF A FILE
def viewContents(dirName):
    lyst = list(filter(os.path.isfile, os.listdir(dirName)))
    if len(lyst) == 0:
        print("There are no files in this directory")
    else:
        while True:
            print(f"Files in {dirName}:\n")
            for element in lyst: print(element)
            fileName = input("\nEnter a file name to view contents: ")
            if not fileName in lyst:
                print("Sorry, there is an error in your file name.")
            else:
                f = open(fileName, 'r')
                print(f.read())
                break

if __name__ == "__main__":
    main()
