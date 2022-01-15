"""
CIAT Class:  ASD210 Fundamentals of Python - First Programs
STUDENT: Felicito A. Rustique
INSTRUCTOR: Nathan Kilgore
ASSIGNMENT: Week2 Part2 Exercise #2
Allows the user to navigate to any line in a text file.
Task to Accomplish
Modify the Base Code so, that the program allows selecting 2 different strings and printing them in one sentence. 
Also, conduct statistic count on symbols in the combined 2 strings.
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

# Take the input file name
inName = input("Enter the input file name: ")

# Open the input file and read the text
inputFile = open(inName, 'r')

lines = [] #LIST CONTAINING EACH LINE OF TEXT
for line in inputFile:
    lines.append(line)

print("\nThe file has", len(lines), "lines of strings.")
print("You can select two of them to combine.")

# Loop for line numbers from the user until 0 entered
# and print the line's number followed by the line
while True:
    if len(lines) == 0:
        break
    firstChoice = int(input("\nEnter first line number [0 to quit]: "))
    if firstChoice == 0:
        break
    elif firstChoice > len(lines):
        print("ERROR: line number must be less than", len(lines))
    else:
        print(firstChoice, ": ", (lines[firstChoice-1]))

    secondChoice = int(input("\nEnter second line number [0 to quit]: "))
    if secondChoice == 0:
        break
    elif secondChoice > len(lines):
        print("ERROR: line number must be less than", len(lines))
    else:
        print(secondChoice, ": ", (lines[secondChoice-1]))
        break

#COMBINE SELECTED LINE STRINGS INTO ONE. ENSURE NEWLINE CHARACTERS ARE REMOVED SO OUTPUT IS ONE LINE:     
combinedLines = lines[firstChoice-1].strip('\n') + " " + lines[secondChoice-1].strip('\n')

#CONDUCT STATISTIC COUNT ON SYMBOLS IN THE COMBINED 2 STRINGS:
charCount = 0
for ch in combinedLines:
    charCount += 1

print(f"\nLines {firstChoice} + {secondChoice} printed as one is: ")
print(f"{combinedLines}")
print(f"\nThere are {charCount} characters, including whitespaces, in the combined lines.\n")
