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
Complete project 6: The kinetic energy of a moving object is given by the formula KE = (1/2)*mv(squared)
where m is the object’s mass and v is its velocity.
Modify the program you created in Project 5 so that it prints the object’s kinetic energy as well as its momentum. 
"""
print("Pg. 62, Project 6:")
mass = float(input("Enter the mass in kilograms of your object: "))
velocity = float(input("\nEnter the velocity of your object as meters per second: "))
momentum = mass * velocity
kineticEnergy = (mass * pow(velocity,2))/2
print("Your object's momentum, which is mass * velocity, is: ", float(momentum))
print("Your object's kinetic energy is: ", float(kineticEnergy))


"""
Complete project 10: An employee’s total weekly pay equals the hourly wage multiplied by the total number of regular hours
plus any overtime pay.
Overtime pay equals the total overtime hours multiplied by 1.5 times the hourly wage.
Write a program that takes as inputs the hourly wage, total regular hours, and total overtime hours
and displays an employee’s total weekly pay. 
"""
print("\nPg. 63, Project 10:")
hrWage = float(input("Enter hourly wage: "))
regHrs = float(input("Enter total regular hours worked: "))
overHrs = float(input("Enter total overtime hours worked: "))
overPay = overHrs * (1.5 * hrWage)
weeklyPay = (hrWage * regHrs) + overPay
print("\nYour total weekly pay is: $",weeklyPay)

#From Pg. 100 & 101 of the text:
"""
Complete project 8: The greatest common divisor of two positive integers, A and B, is the largest number 
that can be evenly divided into both of them.
Euclid’s algorithm can be  used to find the greatest common divisor (GCD) of two positive integers. 
You can use this algorithm in the following manner:
a. Compute the remainder of dividing the larger number by the smaller number.
b. Replace the larger number with the smaller number and the smaller number  with the remainder.  
c. Repeat this process until the smaller number is zero. The larger number at this point is the GCD of A and B. 
Write a program that lets the user enter two integers and then prints each step in the process of using
the Euclidean algorithm to find their GCD. 
"""
print("\nPg. 100, Project 8:")
int1 = int(input("Enter first integer: "))
int2 = int(input("Enter second integer: "))
if int1 > int2:
    largerNum = int1
    smallerNum = int2
    while smallerNum != 0:          
        remainder = largerNum%smallerNum
        print("\nThe remainder of dividing the larger number by the smaller number is: ", remainder)
        largerNum = smallerNum
        print("The larger number is now: ", largerNum)
        smallerNum = remainder
        print("The smaller number is now: ", smallerNum)
        if smallerNum == 0:
            print("\nBecause the smaller number is now 0,")
            print(largerNum," is the GCD of ", int1 ," and ", int2 ,".")
            print("")
elif int2 > int1:
    largerNum = int2
    smallerNum = int1
    while smallerNum != 0:          
        remainder = largerNum%smallerNum
        print("\nThe remainder of dividing the larger number by the smaller number is: ", remainder)
        largerNum = smallerNum
        print("The larger number is now: ", largerNum)
        smallerNum = remainder
        print("The smaller number is now: ", smallerNum)
        if smallerNum == 0:
            print("\nBecause the smaller number is now 0,")
            print(largerNum," is the GCD of ", int2 ," and ", int1 ,".")
            print("")
else:
    print("You didn't enter 2 different numbers.")
    
"""
Complete project 9: Write a program that receives a series of numbers from the user and allows the user
to press the enter key to indicate that he or she is finished providing inputs.
After the user presses the enter key, the program should print the sum of the  numbers and their average. 
"""
print("\nPg. 101, Project 9:")
sum = 0
count = 0
average = 0
numArray = []
data = float(input("""Enter your series of numbers one at a time.
When done, hit Enter a second time: """))
while data != "":
    number = float(data)
    sum += number
    count = count + 1
    average = sum / count
    numArray.append(number)
    for i in numArray:
        print(i, end = " ")
    data = input()
print("The sum of your numbers is: ", sum)
print("The average of your numbers is: ", round(average, 2))
        
"""
Complete project 10: The credit plan at TidBit Computer Store specifies a 10% down payment and an annual interest rate of 12%.
Monthly payments are 5% of the listed purchase price, minus the down payment. 
Write a program that takes the purchase price as input. 
The program should display a table, with appropriate headers, of a payment schedule for the lifetime of the loan. 
Each row of the table should contain  the following items: 
• the month number (beginning with 1) 
• the current total balance owed • the interest owed for that month 
• the amount of principal owed for that month • the payment for that month 
• the balance remaining after payment. The amount of interest for a month is equal to balance * rate/12. 
The amount of principal for a month is equal to the monthly payment minus the interest owed. 
"""
print("\nPg. 101, Project 10:")
#CREATE CONSTANTS:
DOWNPAYMENT = .1
ANNUALINTRATE = .12
#PROMPT TO ENTER PURCHASE PRICE TO SET MONTHLY PAYMENT:
pPrice = float(input("Enter the purchase price: "))
mnthNum = 0
crntBalance = pPrice - (.1 * pPrice) #the current total balance owed
print("\nAfter a 10% down payment, your payment plan is: ")
#PRINT COLUMN HEADERS:
print("\nMONTH  BALANCE     INTEREST   PRINCIPAL   PAYMENT   REMAINING BALANCE\n")
#ENTER WHILE LOOP TO CREATE AMOUNTS FOR TABLE:
while crntBalance > 0:
    mnthNum += 1 #the month number (beginning with 1)
    #crntBalance = pPrice - (.1 * pPrice) #the current total balance owed
    MONTHPAYMENT = .05 * (pPrice - (.1 * pPrice)) #the payment for that month. Monthly payments are 5% of the listed purchase price, minus the down payment. 
    mnthInterest = crntBalance * (ANNUALINTRATE/12) #the interest owed for that month. The amount of interest for a month is equal to balance * rate/12.
    mnthInterest = round(mnthInterest, 2) #Round the float to two decimals
    mnthPrincipal = MONTHPAYMENT - mnthInterest #the amount of principal owed for that month. The amount of principal for a month is equal to the monthly payment minus the interest owed
    mnthPrincipal = round(mnthPrincipal, 2) #Round the float to two decimals
    postBalance = crntBalance - MONTHPAYMENT + mnthInterest #the balance remaining after payment
    postBalance = round(postBalance, 2)
    #PRINT DATA FOR THE REQUIRED COLUMN HEADERS:
    print("%-7d%-12.2f%-11.2f%-12.2f%-10.2d%-17.2f" % (mnthNum, crntBalance, mnthInterest, mnthPrincipal, MONTHPAYMENT, postBalance))
    crntBalance = postBalance
print("")

