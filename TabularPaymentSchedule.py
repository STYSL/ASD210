"""
Complete project 10: The credit plan at TidBit Computer Store specifies a 10% down payment and an annual interest rate of 12%. Monthly payments are 5% of the listed purchase price, minus the down payment. Write a program that takes the purchase price as input. The program should display a table, with appropriate headers, of a payment schedule for the lifetime of the loan. Each row of the table should contain  the following items: • the month number (beginning with 1) • the current total balance owed • the interest owed for that month • the amount of principal owed for that month • the payment for that month • the balance remaining after payment. The amount of interest for a month is equal to balance * rate/12. The amount of principal for a month is equal to the monthly payment minus the interest owed. 
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

#CREATE CONSTANTS:
DOWNPAYMENT = .1
ANNUALINTRATE = .12
#PROMPT TO ENTER PURCHASE PRICE TO SET MONTHLY PAYMENT:
pPrice = float(input("Enter the purchase price: "))
mnthNum = 0
crntBalance = pPrice - (.1 * pPrice) #the current total balance owed
#PRINT COLUMN HEADERS:
print("\nAfter a 10% down payment, your payment plan is: ")
print("\nMONTH  BALANCE     INTEREST   PRINCIPAL   PAYMENT   REMAINING BALANCE\n")
#ENTER WHILE LOOP:

while crntBalance > 0:
    #CREATE THE REQUIRED COLUMN HEADERS:
    mnthNum += 1 #the month number (beginning with 1)
    #crntBalance = pPrice - (.1 * pPrice) #the current total balance owed
    MONTHPAYMENT = .05 * (pPrice - (.1 * pPrice)) #the payment for that month. Monthly payments are 5% of the listed purchase price, minus the down payment. 
    mnthInterest = crntBalance * (ANNUALINTRATE/12) #the interest owed for that month. The amount of interest for a month is equal to balance * rate/12.
    mnthInterest = round(mnthInterest, 2) #Round the float to two decimals
    mnthPrincipal = MONTHPAYMENT - mnthInterest #the amount of principal owed for that month. The amount of principal for a month is equal to the monthly payment minus the interest owed
    mnthPrincipal = round(mnthPrincipal, 2) #Round the float to two decimals
    postBalance = crntBalance - MONTHPAYMENT + mnthInterest #the balance remaining after payment
    postBalance = round(postBalance, 2)
    print("%-7d%-12.2f%-11.2f%-12.2f%-10.2d%-17.2f" % (mnthNum, crntBalance, mnthInterest, mnthPrincipal, MONTHPAYMENT, postBalance))
    crntBalance = postBalance
print("")