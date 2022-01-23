"""
File: viewfiles.py
Project 6.7

Allows the user to visit all of the files in the current path and view them.

"""

import os, os.path

def main():
    viewFiles(os.getcwd())
    
def viewFiles(path):
    """Visits all of the files and directories in
    path and displays the files' contents."""
    if os.path.isfile(path):
        print("File name: " + path)
        f = open(path, 'r')
        print(f.read())
    else:
        print("Directory name: " + path)
        list = os.listdir(path)
        for element in list: viewFiles(element)

if __name__ == "__main__":
    main()
