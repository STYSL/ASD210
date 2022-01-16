"""
CIAT Class:  ASD210 Fundamentals of Python - First Programs
STUDENT: F.Rustique Jr.
INSTRUCTOR: Nathan Kilgore
ASSIGNMENT: Week2 Part1 Assignment: Programming Challenge
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

#GENERATE 15 RANDOM NUMBERS RANGING FROM 1 TO 99:
lottoNumbers = []
loopNumber = 1
while loopNumber < 16:
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
  
#GROUP THE RANDOM NUMBERS INTO 3 SETS OF 5:
set1 = lottoNumbers[0:5] #First 5 numbers
set2 = lottoNumbers[5:10] #Second 5 numbers
set3 = lottoNumbers[-5:] #Last 5 numbers

#MAKE A COPY OF THE LOTTO NUMBERS TO USE WHILE GUESSING:
lottoNumbersCopy = lottoNumbers

print("THE LOTTERY GUESSING GAME\n")

#CREATE A DISPLAY OF THE CORRELATED, MASKED LOTTERY NUMBERS:
maskedNumbers = []
for x in range(15):
    maskedNumbers.append('?')
set1Masked = maskedNumbers[0:5]
set2Masked = maskedNumbers[5:10]
set3Masked = maskedNumbers[-5:]
print(f"Set 1: {set1Masked}")
print(f"Set 2: {set2Masked}")
print(f"Set 3: {set3Masked}")

#LOTTERY GAME EXPLANATION:
print("\nFifteen random lotto numbers, each from 1 to 99 have been generated.")
print("The numbers have been placed into 3 sets of 5.")
print("You have 10 guesses to try and match as many of the numbers in the 3 sets.")
#print("""Any matches as you guess will be displayed.""")

#ARRAY TO CONTAIN 10 GUESSES AND PRINT:
guessedNumbers = [] 

#ARRAY TO CONTAIN MATCHES:
matchedNumbers = []

#MAKE 10 GUESSES:
guessCount = 1
matches = 0
while guessCount < 11:
    print(f"\nMatches made: {matches}")
    print("Guess attempt #:", guessCount)
    numGuess = int(input(f"Enter your guess: "))
    guessedNumbers.append(numGuess)
    print(f"Guesses: {guessedNumbers[0:]}")
    guessCount += 1
    #for numbers in lottoNumbers: 
    if numGuess in lottoNumbersCopy:
        clearConsole()       
        print("\nYou made a match!")
        #Change the correlated masked number to the matched lotto number:
        index = lottoNumbers.index(numGuess)
        maskedNumbers[index] = numGuess
        matchedNumbers.append(numGuess)
        matches += 1
        #remove the correctly guessed number:
        lottoNumbersCopy.remove(numGuess)
    else:
        clearConsole()
        print("\nSorry. No match.")
    
    print("\nTHE LOTTERY GUESSING GAME\n")
    set1Masked = maskedNumbers[0:5]
    set2Masked = maskedNumbers[5:10]
    set3Masked = maskedNumbers[-5:]
    print(f"Set 1: {set1Masked}")
    print(f"Set 2: {set2Masked}")
    print(f"Set 3: {set3Masked}")
    print(f"\nGuesses: {guessedNumbers[0:]}")
      
print("\nYou made 10 guesses.")
print("\nWinning lottery numbers: ")
print(f"Set 1: {set1}")
print(f"Set 2: {set2}")
print(f"Set 3: {set3}")
print(f"\nYou made {matches} matches: {matchedNumbers} ")
print("\nThanks for playing!\n")