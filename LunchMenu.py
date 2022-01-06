"""
CIAT Class:  ASD210 Fundamentals of Python - First Programs
STUDENT: Felicito A. Rustique
INSTRUCTOR: Nathan Kilgore
ASSIGNMENT: Week1 Part1 Discussion

Propose a menu-driven program that calculates the total price for a picnic lunch that the user is purchasing for a group of friends.

The user is first asked to enter her budget for the lunch. She/he has the option of buying apples, cheese, and bread. Set the price per apple, price per pound of cheese, and price per loaf of bread in constant variables.
Use a nested repetition/selection structure to ask the user what type of item and how much of each item she would like to purchase. Keep a running total of the items purchased inside the loop. Exit the loop if the total has exceeded the user’s budget. In addition, provide a sentinel value that allows the user to exit the purchasing loop at any time. Post either flowchart or pseudocode (structured English) to demonstrate your proposed solution concept. The Python code with program execution print screen is even more appreciated!
"""

#IMPORT SYS OBJECT TO USE EXIT METHOD:
import sys

#import os to use clearConsole method:
import os

#clearConsole clears screen output
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
    
clearConsole()

#DECLARE VARIABLES TO USE DURING PROGRAM:
#SET CONSTANT VARIABLES FOR PRICE PER APPLE, POUND OF CHEESE, AND LOAF OF BREAD:
APPLEPRICE = 1.50
CHEESEPRICE = 3.50
BREADPRICE = 3.25 

#SET VARIABLE FOR NUMBER OF AN ITEM REQUESTED TO ZERO:
numRequest = 0

#SET VARIABLES OF TOTAL APPLES, TOTAL CHEESE, AND TOTAL BREAD ORDERED TO ZERO: 
numApples = 0
numCheese = 0
numBread = 0

#SET VARIABLES FOR TOTAL COST OF EACH ITEM ORDERED
totalCostApples = numApples * APPLEPRICE
totalCostCheese = numCheese * CHEESEPRICE
totalCostBread = numBread * BREADPRICE

#SET GRAND TOTAL TO EQUAL TOTAL COST OF ITEMS ORDERED
grandTotal = (totalCostApples + totalCostCheese + totalCostBread)
 
menuChoice = "" #SET MENU CHOICE VARIABLE TO BLANK
SENTINEL = 'D' #SET SENTINEL VALUE AS 'D'

#GREET AND PRESNT CUSTOMER MENU OPTIONS OF APPLES, CHEESE, OR BREAD FOR LUNCH AND GIVE PRICES FOR EACH ITEM:
print("Hello. You can place a lunch order here.")
print("Your options are Apples for $1.25 each.")
print("Cheese for $3.50 per pound.")
print("Bread for $3.25 per loaf.")

#PROMPT CUSTOMER TO ENTER LUNCH BUDGET AMOUNT IF THEY WANT TO PROCEED AND PLACE AN ORDER, OR '0' TO QUIT AND EXIT PROGRAM.
BUDGET = float(input("\nPlease enter how much you want to spend or enter '0' to quit: "))

#IF LUNCH BUDGET ENTRY IS '0', SAY GOOD-BYE AND EXIT PROGRAM WITH EXIT() METHOD:
if BUDGET == 0:
    print("\nGood-Bye")
    exit()

#EXECUTE WHILE LOOP WITH CONDITION OF MENU CHOICE NOT 'D':
while menuChoice != 'D':
    #try:
        #PROMPT CUSTOMER TO CHOOSE MENU ITEM OF APPLES, CHEESE, OR BREAD, OR 'D' FOR DONE AND TO BREAK:
        print("")
        menuChoice = input("\nTo order, enter 'A' for apples, 'B' for bread, or 'C' for cheese. \nEnter 'D' when done: ").upper()
        if menuChoice == 'A':
            numRequest = int(input("\nEnter number of apples to add to order: "))
            numApples += numRequest #CALCULATE TOTAL APPLES ORDERED
            totalCostApples = 0 #ENSURE TOTAL COST OF ITEM ORDERED RESETS TO ZERO BEFORE RECALULATING TOTAL
            totalCostApples = numApples * APPLEPRICE #CALCULATE TOTAL COST OF APPLES
            grandTotal = (totalCostApples + totalCostCheese + totalCostBread) #CALCULATE TOTAL ORDER OF ALL ITEMS
            balance = BUDGET - grandTotal
            
            #IF BALANCE IS LESS THAN ZERO, DISPLAY NEGATIVE BUDGET, CANCEL LAST REQUEST:
            if balance < 0:
                print("\nYou now have a balance of $", balance ,". Your last entry cannot be added to your order")
                balance += numRequest * APPLEPRICE #ADD BACK LAST ORDER REQUEST
                numApples -= numRequest #REMOVE LAST NUMBER OF APPLES REQUESTED FROM TOTAL APPLES REQUESTED
                totalCostApples = numApples * APPLEPRICE #UPDATE TOTAL COST OF APPLES
                grandTotal = (totalCostApples + totalCostCheese + totalCostBread)
                print("\nYour current order is $", grandTotal, "for: ")
                print(numApples, "Apples: $", totalCostApples)
                print(numCheese, "Pounds of Cheese: $", totalCostCheese)
                print(numBread, "Loaves of Bread: $", totalCostBread)
                print("Remaining budget: $",balance)
                continue #CONTINUE PLACING ORDER UNTIL 'D' ENTERED
            
            #IF BALANCE STILL POSITIVE, DISPALY ORDER OVERVIEW AND REMAINING BUDGET:
            elif balance > 0:
                print("\nYour current order is $", grandTotal, "for: ")
                print(numApples, "Apples: $", totalCostApples)
                print(numCheese, "Pounds of Cheese: $", totalCostCheese)
                print(numBread, "Loaves of Bread: $", totalCostBread)
                print("Remaining budget: $",balance)
            else:
                continue #CONTINUE PLACING ORDER UNTIL 'D' ENTERED

        if menuChoice == 'B':
            numRequest = int(input("\nEnter loaves of bread to add to order: "))
            numBread += numRequest #CALCULATE TOTAL LOAVES OF BREAD ORDERED
            totalCostBread = 0 #ENSURE TOTAL COST OF ITEM ORDERED RESETS TO ZERO BEFORE RECALULATING TOTAL
            totalCostBread = numBread * BREADPRICE #CALCULATE TOTAL COST OF BREAD
            grandTotal = (totalCostApples + totalCostCheese + totalCostBread) #CALCULATE TOTAL ORDER OF ALL ITEMS
            balance = BUDGET - grandTotal
            
            #IF BUDGET IS LESS THAN ZERO, DISPLAY NEGATIVE BUDGET, CANCEL LAST REQUEST:
            if balance < 0:
                print("\nYou now have a balance of $", balance ,". Your last entry cannot be added to your order.")
                balance += numRequest * BREADPRICE #ADD BACK LAST ORDER REQUEST
                numBread -= numRequest #REMOVE LAST NUMBER OF BREAD REQUESTED FROM TOTAL BREAD REQUESTED
                totalCostBread = numBread * BREADPRICE #UPDATE TOTAL COST OF BREAD
                grandTotal = (totalCostApples + totalCostCheese + totalCostBread)
                print("\nYour current order is $", grandTotal, "for: ")
                print(numApples, "Apples: $", totalCostApples)
                print(numCheese, "Pounds of Cheese: $", totalCostCheese)
                print(numBread, "Loaves of Bread: $", totalCostBread)
                print("Remaining budget: $",balance)
                print("")
                continue #CONTINUE PLACING ORDER UNTIL 'D' ENTERED
            
            #IF BUDGET STILL POSITIVE, CURRENT ORDER OVERVIEW AND REMAINING BUDGET:
            elif balance > 0:
                print("Your current order is $", grandTotal, "for: ")
                print(numApples, "Apples: $", totalCostApples)
                print(numCheese, "Pounds of Cheese: $", totalCostCheese)
                print(numBread, "Loaves of Bread: $", totalCostBread)
                print("Remaining budget: $",balance)
            else:
                continue #CONTINUE PLACING ORDER UNTIL 'D' ENTERED
            
        if menuChoice == 'C':
            numRequest = int(input("\nEnter pounds of cheese to add to order: "))
            numCheese += numRequest #CALCULATE TOTAL POUNDS OF CHEESE ORDERED
            totalCostCheese = 0 #ENSURE TOTAL COST OF ITEM ORDERED RESETS TO ZERO BEFORE RECALULATING TOTAL
            totalCostCheese = numCheese * CHEESEPRICE #CALCULATE TOTAL COST OF CHEESE
            grandTotal = (totalCostApples + totalCostCheese + totalCostBread) #CALCULATE TOTAL ORDER OF ALL ITEMS
            balance = BUDGET - grandTotal
            
            #IF BALANCE IS LESS THAN ZERO, DISPLAY NEGATIVE BALANCE, CANCEL LAST REQUEST:
            if balance < 0:
                print("\nYou now have a balance of $", balance ,". Your last entry cannot be added to your order")
                balance += numRequest * CHEESEPRICE #ADD BACK LAST ORDER REQUEST
                numCheese -= numRequest #REMOVE LAST NUMBER OF CHEESE REQUESTED FROM TOTAL CHEESE
                totalCostCheese = numCheese * CHEESEPRICE #UPDATE TOTAL COST OF CHEESE
                grandTotal = (totalCostApples + totalCostCheese + totalCostBread)
                print("\nYour current order is $", grandTotal, "for: ")
                print(numApples, "Apples: $", totalCostApples)
                print(numCheese, "Pounds of Cheese: $", totalCostCheese)
                print(numBread, "Loaves of Bread: $", totalCostBread)
                print("Remaining budget: $",balance)
                continue #CONTINUE PLACING ORDER UNTIL 'D' ENTERED
            
            #IF BALANCE STILL POSITIVE, DISPALY ORDER OVERVIEW AND REMAINING BUDGET:
            elif balance > 0:
                print("\nYour current order is $", grandTotal, "for: ")
                print(numApples, "Apples: $", totalCostApples)
                print(numCheese, "Pounds of Cheese: $", totalCostCheese)
                print(numBread, "Loaves of Bread: $", totalCostBread)
                print("Remaining budget: $",balance)
            else:
                continue #CONTINUE PLACING ORDER UNTIL 'D' ENTERED     
        #print(f"\nInvalid entry. Try again.")
    #except Exception as e:
        #print(e)
           
#ONCE OUTSIDE WHILE LOOP:
print("\nCurrent order placed. Thank you.")
exit()