"""
CIAT Class:  ASD210 Fundamentals of Python - First Programs
STUDENT: Felicito A. Rustique
INSTRUCTOR: Nathan Kilgore
ASSIGNMENT: Week1 Part1 Discussion

Propose a menu-driven program that calculates the total price for a picnic lunch that the user is purchasing for a group of friends.

The user is first asked to enter her budget for the lunch. She/he has the option of buying apples, cheese, and bread. Set the price per apple, price per pound of cheese, and price per loaf of bread in constant variables.
Use a nested repetition/selection structure to ask the user what type of item and how much of each item she would like to purchase. Keep a running total of the items purchased inside the loop. Exit the loop if the total has exceeded the user’s budget. In addition, provide a sentinel value that allows the user to exit the purchasing loop at any time. Post either flowchart or pseudocode (structured English) to demonstrate your proposed solution concept. The Python code with program execution print screen is even more appreciated!

PSEUDOCODE/ALGORITHM 
(Outlined as numbered steps):

1. IMPORT SYS OBJECT TO USE EXIT METHOD:

2. DECLARE VARIABLES TO USE DURING PROGRAM:
    2A. SET CONSTANT VARIABLES FOR PRICE PER APPLE, POUND OF CHEESE, AND LOAF OF BREAD:
    2B. SET VARIABLES OF REQUESTED APPLES, CHEESE AND BREAD TO USE WHILE INSIDE LOOP TO ZERO:
    2E. SET VARIABLES OF TOTAL APPLES, TOTAL CHEESE, AND TOTAL BREAD ORDERED TO ZERO:
    2F. SET TOTAL ORDER VARIABLE TO ZERO:
    2G. SET MENU CHOICE VARIABLE TO BLANK:
    2G. SET SENTINEL VALUE AS 'D':

3. GREET AND PRESNT CUSTOMER MENU OPTIONS OF APPLES, CHEESE, OR BREAD FOR LUNCH AND GIVE PRICES FOR EACH ITEM:

4. PROMPT CUSTOMER TO ENTER LUNCH BUDGET AMOUNT IF THEY WANT TO PROCEED AND PLACE AN ORDER, OR '0' TO QUIT AND EXIT PROGRAM.

5. IF LUNCH BUDGET ENTRY IS '0', SAY GOOD-BYE AND EXIT PROGRAM WITH EXIT() METHOD:

6. EXECUTE WHILE LOOP WITH CONDITION OF MENU CHOICE NOT 'D':
    6A. PROMPT CUSTOMER TO CHOOSE MENU ITEM OF APPLES, CHEESE, OR BREAD, OR 'D' FOR DONE AND TO BREAK:
    
    7. IF APPLES SELECTED, PROMPT CUSTOMER TO ENTER NUMBER OF APPLES REQUESTED:
        7A. CALCULATE COST OF REQUESTED APPLES (appleRequestCost = requestedApples * pricePerApple)
        7B. CALCULATE TOTAL APPLES ORDERED (totalReqeustedApples += requestedApples)
        7C. CALCULATE TOTAL COST OF APPLES (totalAppleCost += appleRequestCost)
        7D. CALCULATE TOTAL ORDER OF ALL ITEMS (grandTotal = totalAppleCost + totalCheeseCost + totalBreadCost)
        7E. UPDATE BUDGET (budget -= grandTotal)
        
        7F. IF BUDGET IS LESS THAN ZERO, CANCEL LAST REQUEST:
            7G. DISPLAY NEGATIVE BUDGET
            7H. TELL CUSTOMER LAST ITEM ORDER CANNOT BE PLACED DUE TO INSUFFICIENT BUDGET
            7I. ADD BACK GRAND TOTAL AND UPDATE BUDGET (budget += grandTotal)
            7J. REMOVE LAST NUMBER OF APPLES REQUESTED FROM TOTAL APPLES REQUESTED:
            (totalRequestedApples -= requestedApples)
            7K. UPDATE TOTAL NUMBER OF APPLES ORDERED (totalRequestedApples -= requestedApples)
            7L. UPDATE TOTAL COST OF APPLES (totalAppleCost -= appleRequestCost)
            7M. BREAK FROM WHILE LOOP TO DISPLAY FINAL ORDER
        
        7N. IF BUDGET STILL POSITIVE, DISPLAY TOTAL OF APPLES REQUESTED AND TOTAL COST OF APPLES TO CUSTOMER:
        7O. DISPLAY CURRENT ORDER TOTAL AND CURRENT BUDGET TO CUSTOMER
        7P. PROMPT CUSTOMER TO ENTER 'D' IF DONE TO COMPLETE ORDER OR HIT ENTER TO CONTINUE:
        7Q. IF 'D' ENTERED, BREAK
        
        
    8. IF CHEESE SELECTED, PROMPT CUSTOMER TO ENTER NUMBER OF POUNDS OF CHEESE REQUESTED:
        8A. CALCULATE COST OF REQUESTED APPLES (cheeseRequestCost = requestedcheese * pricePerCheese)
        8B. CALCULATE TOTAL APPLES ORDERED (totalReqeustedCheese += requestedCheese)
        8C. CALCULATE TOTAL COST OF APPLES (totalCheeseCost += cheeseRequestCost)
        8D. CALCULATE TOTAL ORDER OF ALL ITEMS (grandTotal = totalAppleCost + totalCheeseCost + totalBreadCost)
        8E. UPDATE BUDGET (budget -= grandTotal)
        
        8F. IF BUDGET IS LESS THAN ZERO, CANCEL LAST REQUEST:
            8G. DISPLAY NEGATIVE BUDGET
            8H. TELL CUSTOMER LAST ITEM ORDER CANNOT BE PLACED DUE TO INSUFFICIENT BUDGET
            8I. ADD BACK GRAND TOTAL AND UPDATE BUDGET (budget += grandTotal)
            8J. REMOVE LAST NUMBER OF CHEESE REQUESTED FROM TOTAL OF CHEESE REQUESTED:
            (totalReequestedCheese -= requestedCheese)
            8K. UPDATE TOTAL NUMBER OF CHEESE ORDERED (totalRequestedCheese -= requestedCheese)
            8L. UPDATE TOTAL COST OF CHEESE (totalCheeseCost -= cheeseRequestCost)
            8M. BREAK FROM WHILE LOOP TO DISPLAY FINAL ORDER
        
        8N. IF BUDGET STILL POSITIVE, DISPLAY TOTAL OF CHEESE REQUESTED AND TOTAL COST OF CHEESE TO CUSTOMER:
        8O. DISPLAY CURRENT ORDER TOTAL AND CURRENT BUDGET TO CUSTOMER
        8P. PROMPT CUSTOMER TO ENTER 'D' IF DONE TO COMPLETE ORDER OR HIT ENTER TO CONTINUE:
        8Q. IF 'D' ENTERED, BREAK

    9. IF BREAD SELECTED, PROMPT CUSTOMER TO ENTER NUMBER OF BREAD REQUESTED:
        9A. CALCULATE COST OF REQUESTED BREAD (breadRequestCost = requestedBread * pricePerbread)
        9B. CALCULATE TOTAL BREAD ORDERED (totalReqeustedBread += requestedBread)
        9C. CALCULATE TOTAL COST OF BREAD (totalBreadCost += breadRequestCost)
        9D. CALCULATE TOTAL ORDER OF ALL ITEMS (grandTotal = totalAppleCost + totalCheeseCost + totalBreadCost)
        9E. UPDATE BUDGET (budget -= grandTotal)
        
        9F. IF BUDGET IS LESS THAN ZERO, CANCEL LAST REQUEST:
            9G. DISPLAY NEGATIVE BUDGET
            9H. TELL CUSTOMER LAST ITEM ORDER CANNOT BE PLACED DUE TO INSUFFICIENT BUDGET
            9I. ADD BACK GRAND TOTAL AND UPDATE BUDGET (budget += grandTotal)
            9J. REMOVE LAST NUMBER OF BREAD REQUESTED FROM TOTAL BREAD REQUESTED:
            (totalRequestedBread -= requestedBread)
            9K. UPDATE TOTAL NUMBER OF BREAD ORDERED (totalRequestedBread -= requestedBread)
            9L. UPDATE TOTAL COST OF BREAD (totalBreadCost -= breadRequestCost)
            9M. BREAK FROM WHILE LOOP TO DISPLAY FINAL ORDER
        
        9N. IF BUDGET STILL POSITIVE, DISPLAY TOTAL OF BREAD REQUESTED AND TOTAL COST OF BREAD TO CUSTOMER:
        9O. DISPLAY CURRENT ORDER TOTAL AND CURRENT BUDGET TO CUSTOMER
        9P. PROMPT CUSTOMER TO ENTER 'D' IF DONE TO COMPLETE ORDER OR HIT ENTER TO CONTINUE:
        9Q. IF 'D' ENTERED, BREAK

10. ONCE OUTSIDE WHILE LOOP:

    10A. DISPLAY TOTAL NUMBER OF EACH PRODUCT ORDERED AND THE PRODUCTS TOTAL COST
    10B. DISPLAY THE TOTAL OF ENTIRE ORDER
    10C. DISPLAY THE REMAINING BUDGET.

"""