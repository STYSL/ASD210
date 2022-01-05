"""
CIAT Class:  ASD210 Fundamentals of Python - First Programs
STUDENT: Felicito A. Rustique
INSTRUCTOR: Nathan Kilgore
ASSIGNMENT: Week1 Part2 HandsOn
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

#From Pg. 62 & 63 of the text:
"""
Complete project 6: The kinetic energy of a moving object is given by the formula KE = (1/2)*mv(squared) where m is the object’s mass and v is its velocity. Modify the program you created in Project 5 so that it prints the object’s kinetic energy as well as its momentum. 
"""

mass = float(input("Enter the mass in kilograms of your object: "))
velocity = float(input("Enter the velocity of your object as meters per second: "))
momentum = mass * velocity
kineticEnergy = (mass * pow(velocity,2))/2
print("Your object's momentum, which is mass * velocity, is: ", float(momentum))
print("Your object's kinetic energy is: ", float(kineticEnergy))
print("") #SKIP A CONSOLE LINE FOR EASIER VIEWING


"""
Complete project 10: An employee’s total weekly pay equals the hourly wage multiplied by the total number of regular hours plus any overtime pay. Overtime pay equals the total overtime hours multiplied by 1.5 times the hourly wage. Write a program that takes as inputs the hourly wage, total regular hours, and total overtime hours and displays an employee’s total weekly pay. 
"""




#From Pg. 100 & 101 of the text:
"""
Complete project 8: The greatest common divisor of two positive integers, A and B, is the largest  number that can be evenly divided into both of them. Euclid’s algorithm can be  used to find the greatest common divisor (GCD) of two positive integers. You  can use this algorithm in the following manner:  a. Compute the remainder of dividing the larger number by the smaller  number.  b. Replace the larger number with the smaller number and the smaller number  with the remainder.  c. Repeat this process until the smaller number is zero. The larger number at this point is the GCD of A and B. Write a program that lets  the user enter two integers and then prints each step in the process of using the  Euclidean algorithm to find their GCD. 
"""

"""
Complete project 9: Write a program that receives a series of numbers from the user and allows the  user to press the enter key to indicate that he or she is finished providing inputs.  After the user presses the enter key, the program should print the sum of the  numbers and their average. 
"""

"""
Complete project 10: The credit plan at TidBit Computer Store specifies a 10% down payment and  an annual interest rate of 12%. Monthly payments are 5% of the listed purchase  price, minus the down payment. Write a program that takes the purchase price  as input. The program should display a table, with appropriate headers, of a payment schedule for the lifetime of the loan. Each row of the table should contain  the following items:  • the month number (beginning with 1)  • the current total balance owed  • the interest owed for that month  • the amount of principal owed for that month  • the payment for that month  • the balance remaining after payment  The amount of interest for a month is equal to balance * rate/ 12. The amount of  principal for a month is equal to the monthly payment minus the interest owed. 
"""