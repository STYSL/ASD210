"""
CIAT Class:  ASD210 Fundamentals of Python - First Programs
STUDENT: Felicito A. Rustique
INSTRUCTOR: Nathan Kilgore
ASSIGNMENT: Week2 Part1 HandsOn
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

#From Pg. 132 & 133 of the text:
"""
Complete project 1: Write a script that inputs a line of plain text
and a distance value and outputs an encrypted text using a Caesar cipher. 
The script should work for any printable characters.
""" 

print("\nThis is project 1:")
plainText = input("\nEnter text you want encrypted: ")
distance = int(input("Enter the distance value: "))
encrypted =  ""
for ch in plainText:
    ordvalue = ord(ch)
    cipherValue = ordvalue + distance
    if cipherValue > ord('z'):
        cipherValue = ord('a') + distance - \
            (ord('z') - ordvalue + 1)
    encrypted += chr(cipherValue)
print(f"'{plainText}' encrypted is: '{encrypted}'\n") 


"""
Complete project 5: A bit shift is a procedure whereby the bits in a bit string are moved to the left or to the right.
For example, we can shift the bits in the string 1011 two places to the left to produce the string 1110. Note that the
leftmost two bits are wrapped around to the right side of the string in this operation. Define two scripts, shiftLeft.py
and shiftRight.py, that expect a bit string as an input. The script shiftLeft shifts the bits in its input one place to
the left, wrapping the leftmost bit  to the rightmost position. The script shiftRight performs the inverse operation.
Each script prints the resulting string. 
"""
print("""\nThis is project 5. Instead of 2 separate files of shiftLeft.py and shiftRight.py, 
shiftLeft and shiftRight were defined as functions: """)

def shiftLeft(bitString):
    shiftedLeft = []
    newBitString = ""
    index = 0
    for chr in range(len(bitString)):
        while index < len(bitString)-1:
            index +=1
            shiftedLeft.append(bitString[index])
    shiftedLeft.append(bitString[0])  
    return newBitString.join(shiftedLeft) 

def shiftRight(bitString):
    shiftedRight = []
    newBitString = ""
    index = -2
    for chr in range(len(bitString)):
        while index < len(bitString)-2:
            index +=1
            shiftedRight.append(bitString[index])
    return newBitString.join(shiftedRight)      

bitString = str(input("""\nEnter a bit string of 1's and 0's.
* Note, this script will still work with any string of characters: """))

print(f"""\nThe characters of {bitString} shifted one place to the left,
with the first character becoming the last, is: {shiftLeft(bitString)}""")

print(f"""\nThe characters of {bitString} shifted one place to the right,
with the last character becoming the first, is: {shiftRight(bitString)}""")

"""
Complete project 8: Write a script named copyfile.py. 
This script should prompt the user for the names of two text files. 
The contents of the first file should be input and written to the second file. 
"""

print("\nProject 8 is a separate file, copyfile.py, as instructed, but also here: ")
filename1 = input("""\nEnter a file name to read input from.
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

print(f"""\n'{filename1}' is saved and copied to '{filename2}', also saved.
Good-Bye.""")


#From Pg. 166 of the text:
"""
Complete project 5: (you may need to complete project 4 from chapter 4 first) In Chapter 4, we developed an algorithm for converting from binary to decimal. You can generalize this algorithm to work for a representation in any base.
Instead of using a power of 2, this time you use a power of the base. Also, you use  digits greater than 9, such as
A... F, when they occur. Define a function named  repToDecimal that expects two arguments, a string, and an integer. 
The second argument should be the base. For example, repToDecimal("10", 8) returns  8, whereas repToDecimal("10", 16)
returns 16. The function should use a lookup table to find the value of any digit. Make sure that this table (it is
actually  a dictionary) is initialized before the function is defined. For its keys, use the 10  decimal digits (all
strings) and the letters A... F (all uppercase). The value stored  with each key should be the integer that the digit
represents. (The letter 'A' associates with the integer value 10, and so on.) The main loop of the function should
convert each digit to uppercase, look up its value in the table, and use this value in the computation. Include a main
function that tests the conversion function with numbers in several bases. 
"""

print("\nProject 5: No thanks. I'll pass on this one for now and take the loss :( ")

"""
Complete project 7: Write a program that inputs a text file. 
The program should print the unique words in the file in alphabetical order. 
"""
print("\nThis is project 7:")
filename1 = input("""\nEnter a file name to read input from.
File will be created if file doesn't exist.
Use '.txt' as the file extension: """)
readInputFile = open(filename1, 'a+')
readInputFile.seek(0)

content = readInputFile.read()
uniqueWords = content.split()
alphabeticalOrder = sorted(uniqueWords)
print(f"""\nThe content of '{filename1}' 
with words in alphabetical order is: """)
for words in alphabeticalOrder:
    print(words)
    
dataEntries = []
data = input(f"""\nIf '{filename1}' is blank, or you want to add to it, enter text now.
Hit 'Enter' two times when finished making entries or once now to skip: """)
while data != "":
    data = ''.join(("\n",data))
    dataEntries.append(data)
    data = input()
readInputFile.writelines(dataEntries)
readInputFile.close()
readInputFile = open(filename1, 'a+')
readInputFile.seek(0)

content = readInputFile.read()
uniqueWords = content.split()
alphabeticalOrder = sorted(uniqueWords)
print(f"""\nThe content of '{filename1}' 
with any new words added and in alphabetical order is: """)
for words in alphabeticalOrder:
    print(words)
    
readInputFile.close()
print(f"\n'{filename1}' is saved and now closed.\nGood-Bye.")