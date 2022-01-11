"""
CIAT Class:  ASD210 Fundamentals of Python - First Programs
STUDENT: F.Rustique Jr.
INSTRUCTOR: Nathan Kilgore
ASSIGNMENT: Week1 Part1 Assignment: Programming Challenge
"""

import random

#import os to use clearConsole method:
import os

#clearConsole clears screen output
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
    
clearConsole()

#GENERATE YOUR 5 RANDOM NUMBERS RANGING FROM 1 TO 99:
lottoNumbers = []
loopNumber = 1
while loopNumber < 6:
    number = random.randint(1, 99)
    lottoNumbers.append(number)
    #ENSURE NO RANDOM NUMBERS ADDED INTO ARRAY ARE DUPLICATES:
    #YOU NEED TO COMPARE THE NUMBER JUST GENERATED WITH THE NUMBERS BEFORE IT,
    #WHICH ARE ALL THE NUMBES IN THE ARRAY LENGTH, MINUS ONE:
    for i in range(len(lottoNumbers)-1): 
        if number == lottoNumbers[i]:
            lottoNumbers.remove(number)
            continue
    else:
        loopNumber += 1
        continue

#BEGIN LOTTERY AND START GUESSING:
print("\nThis is a lottery guessing game.")
print("Five random, lotto numbers, each from 1 to 99 have been generated.")
print("For each number, you have 10 guesses to guess what it is.")
print("""When you are done with all your guesses, 
the lotto numbers and any matches by you will be released.""")

#ARRAY TO CONTAIN FINAL ZEROS OR CORRECT GUESSES AND PRINT AT END:
guessedNumbers = [] 

#MAKE 10 GUESSES FOR 1ST NUMBER:
guessCount = 1
matches = 0
while guessCount < 11:
    print("\nGuess attempt number: ", guessCount)
    firstNumGuess = int(input(f"Enter your guess for the 1st number.\nYou have 10 tries to guess right: "))
    if firstNumGuess == lottoNumbers[0]:
        guessedNumbers.append(firstNumGuess)
        print("You guessed a match!")
        matches = 1
        break
    if firstNumGuess != lottoNumbers[0]:
        guessCount += 1
    #IF ALL 10 GUESSES ARE USED UP, USER GETS A 0 FOR THE FIRST NUMBER FINAL GUESS:
    if guessCount == 10:
        firstNumGuess = 0 
        guessedNumbers.append(firstNumGuess)
    
#MAKE 10 GUESSES FOR 2ND NUMBER:
guessCount = 1
while guessCount < 11:
    print("\nGuess attempt number: ", guessCount)
    secondNumGuess = int(input(f"Enter your guess for the 2nd number.\nYou have 10 tries to guess right: "))
    if secondNumGuess == lottoNumbers[1]:
        guessedNumbers.append(secondNumGuess)
        print("You guessed a match!")
        matches = 2
        break
    if secondNumGuess != lottoNumbers[1]:
        guessCount += 1
    #IF ALL 10 GUESSES ARE USED UP, USER GETS A 0 FOR THE FIRST NUMBER FINAL GUESS:
    if guessCount == 10:
        secondNumGuess = 0
        guessedNumbers.append(secondNumGuess)

#MAKE 10 GUESSES FOR 3RD NUMBER:
guessCount = 1
while guessCount < 11:
    print("\nGuess attempt number: ", guessCount)
    thirdNumGuess = int(input(f"Enter your guess for the 3rd number.\nYou have 10 tries to guess right: "))
    if thirdNumGuess == lottoNumbers[2]:
        guessedNumbers.append(thirdNumGuess)
        print("You guessed a match!")
        matches = 3
        break
    if thirdNumGuess != lottoNumbers[2]:
        guessCount += 1
    #IF ALL 10 GUESSES ARE USED UP, USER GETS A 0 FOR THE FIRST NUMBER FINAL GUESS:
    if guessCount == 10:
        thirdNumGuess = 0
        guessedNumbers.append(thirdNumGuess)

#MAKE 10 GUESSES FOR 4TH NUMBER:
guessCount = 1
while guessCount < 11:
    print("\nGuess attempt number: ", guessCount)
    fourthNumGuess = int(input(f"Enter your guess for the 4th number.\nYou have 10 tries to guess right: "))
    if fourthNumGuess == lottoNumbers[3]:
        guessedNumbers.append(fourthNumGuess)
        print("You guessed a match!")
        matches = 4
        break
    if fourthNumGuess != lottoNumbers[3]:
        guessCount += 1
    #IF ALL 10 GUESSES ARE USED UP, USER GETS A 0 FOR THE FIRST NUMBER FINAL GUESS:
    if guessCount == 10:
        fourthNumGuess = 0
        guessedNumbers.append(fourthNumGuess)
    
#MAKE 10 GUESSES FOR 5TH NUMBER:
guessCount = 1
while guessCount < 11:
    print("\nGuess attempt number: ", guessCount)
    fifthNumGuess = int(input(f"Enter your guess for the 5th number.\nYou have 10 tries to guess right: "))
    if fifthNumGuess == lottoNumbers[4]:
        guessedNumbers.append(fifthNumGuess)
        print("You guessed a match!")
        matches = 5
        break
    if fifthNumGuess != lottoNumbers[4]:
        guessCount += 1
    #IF ALL 10 GUESSES ARE USED UP, USER GETS A 0 FOR THE FIRST NUMBER FINAL GUESS:
    if guessCount == 10:
        fifthNumGuess = 0
        guessedNumbers.append(fifthNumGuess)
    
print("\nYou have finished making all your allowed guesses.")
print("\nThe winning lotto numbers are: ")
print(lottoNumbers, end = " ")
print("")
print("""\nIf you made any correct guesses for a lotto number,
here is where you made them. Incorrect guesses are zero:""")
print(guessedNumbers)
print("\nYou made", matches ,"matches.")
print("\nThanks for playing!\n")