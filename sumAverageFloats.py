"""
Original Program: sum.py
Modified by: F. Rustique,Jr.
Assignment: Week1Part2 Exercise2
Computes the sum and average of a series of input numbers that are only even.
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

theSum = 0
count = 0
while True:
    try:
        number = str(input("Enter a number or press Enter to quit: "))
        #take the string length and subtract 1 to get the last index
        lastDigitIndex = len(number)-1 
        if number == "":
            break
        #EVALUATE MODULUS 2 ON THE LAST DIGIT OF THE NUMBER CONVERTED TO A FLOAT:
        elif (float(number[lastDigitIndex]) % 2 == 0):
            theSum += round(float(number), 2)
            count += 1
            average = theSum / count
        else:
            continue
    except Exception as e:
        print(e)

print(f"\nThe sum of only your even numbers is: {round(theSum, 2)}")
if count > 0:
    print(f"The average of your {count} even numbers is: {round(average, 2)}\n")
