"""
CIAT Class:  ASD210 Fundamentals of Python - First Programs
STUDENT: Felicito A. Rustique
INSTRUCTOR: Nathan Kilgore
ASSIGNMENT: Week2 Part2 HandsOn
"""
#import math library
import math

#import os to use clearConsole method:
import os
#clearConsole clears screen output
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
clearConsole()

"""
1. Write a Python script to concatenate the following dictionaries to create a new one. 

hint: you can convert dictionaries to a list and back to a dictionary by using the list() method and a for loop to assign a key value pair dict[key] = value.

Sample Dictionary:
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
"""
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}
newDictionary = dic1 | dic2 | dic3

print("We have 3 dictionaries as follows:")
print(dic1)
print(dic2)
print(dic3)
print("\nWhen we concatenate these dictionaries the new dictionary is: ")
print(newDictionary)

"""
2. Write a Python script to check if a given key already exists in a dictionary.
"""

#print(newDictionary.get(1, None))
#Another way:

key = int(input("\nEnter a key you are confirming existence for: "))
if key in newDictionary:
    print(f"{key} is a key that exists in the new dictionary")
else:
    print(f"{key} is not a key that exists in the new dictionary")


"""
3. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
Sample Dictionary ( n = 5) :
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
"""

print("""\nWe will now create pairs of numbers where the second number in each pair is
equal to its pair's position in the series times its position.""")
dictionaryLength = int(input("\nEnter how many pairs of numbers you want to see: "))
numberDictionary = {}
for key in range(dictionaryLength):
    key += 1
    numberDictionary[key] = key * key  
print(f"{numberDictionary}\n")
