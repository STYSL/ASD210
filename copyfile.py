"""
CIAT Class: ASD210 Fundamentals of Python - First Programs
STUDENT: Felicito A. Rustique
INSTRUCTOR: Nathan Kilgore
ASSIGNMENT: Week2 Part1 HandsOn
Complete project 8: Write a script named copyfile.py. This script should prompt the user for the names of two text files. The contents of the first file should be input and written to the second file. 
"""
#import os to use clearConsole method:
import os

#clearConsole clears screen output
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
clearConsole()

filename1 = input("""Enter a file name to read input from.
File will be created if file doesn't exist.
Use '.txt' as the file extension: """)
readInputFile = open(filename1, 'a+')

filename2 = input(f"""\nEnter a file name to write content of {filename1} to. 
Use '.txt' as the file extension: """)
writeOutputFile = open(filename2, 'w')

readInputFile.read()
print(f"\nThe content of '{filename1}' is: ")
readInputFile.seek(0)
for line in readInputFile:
    print(line)

dataEntries = []
data = input(f"""\nIf '{filename1}' is blank, or you want to add to it, enter text now.
Hit 'Enter' a second time when done or now to skip: """)
while data != "":
    data = ''.join(("\n",data))
    dataEntries.append(data)
    data = input()
readInputFile.writelines(dataEntries)
        
readInputFile.seek(0)
for line in readInputFile:
    writeOutputFile.write(line)
readInputFile.close()
writeOutputFile.close()

print(f"\n'{filename1} is saved and copied to {filename2}, also saved. Good-Bye.")