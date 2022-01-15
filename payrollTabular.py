"""
CIAT Class: ASD210 Fundamentals of Python - First Programs
STUDENT: Felicito A. Rustique
INSTRUCTOR: Nathan Kilgore
ASSIGNMENT: Week2 Part1 Exercise
Project 4.12
Print a payroll report.
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

# Take the inputs
fileName = input("Enter the file name to open: ")

# Open the input file
inputFile = open(fileName, 'r')

# Read the data and print the report
print()
print("%-7s%-15s%-30s%6s%15s" % ("EmpID", "Name", "Address", "Hours", "Total Pay"))
for line in inputFile:
    dataList = line.split()
    empID = dataList[0]
    name = dataList[1]
    streetNum = dataList[2]
    streetName = dataList[3]
    city = dataList[4]
    state = dataList[5]
    address = (streetNum + ' ' + streetName + ' ' + city + ' ' + state)
    hours = int(dataList[6])
    payRate = float(dataList[7])
    totalPay = hours * payRate
    print("%-7s%-15s%-30s%6s%15.2f" % (empID, name, address, hours, totalPay))
print() 
    
