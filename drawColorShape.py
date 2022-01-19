"""
CIAT Class:  ASD210 Fundamentals of Python - First Programs
STUDENT: Felicito A. Rustique
INSTRUCTOR: Nathan Kilgore
ASSIGNMENT: Week3 Part1 Discussion
"""

#IMPORT TURTLE FROM TURTLE LIBRARY 
from turtle import Turtle

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
Discussion Topic #2:
Write a function that uses the turtle module to draw a simple button (i.e. "Submit" button).
The function should receive the width and height of the button to be drawn, 
as well as the x and y coordinates of the bottom-left corner. 
Explain and share your code in this discussion.
"""

#WRITE A FUNCTION USING THE TURTLE MODULE TO DRAW A SIMPLE BUTTON:
#FUNCTION HAS 6 PARAMETERS:
def drawButton (t, width, height, stroke, fill, coordinates): 
    t.begin_fill() #BEGIN FILL COLORING, HAS TO BE BEFORE OTHER COMMANDS
    t.up() #PEN IS UP TO NOT DRAW
    t.goto(coordinates) #GO TO BOTTOM-LEFT COORDINATES
    t.setheading(0) #DIRECTION TO DRAW WILL BE RIGHT/EAST
    t.down() #SET TURTLE PEN DOWN TO BEGIN DRAWING
    t.pencolor(stroke) #OUTLINE COLOR OF YOUR SHAPE
    t.fillcolor(fill) #FILL COLOR OF YOUR SHAPE
    t.forward(width) #DRAW LINE AS LONG AS WIDTH ARGUMENT PASSED
    t.setheading(90) #TURN 90 DEGREES TO HEAD UP/NORTH
    t.forward(height) #DRAW LINE AS LONG AS HEIGHT ARGUMENT PASSED
    t.setheading(180) #TURN 180 DEGREES TO HEAD LEFT/WEST
    t.forward(width) #DRAW LINE AS LONG AS WIDTH ARGUMENT PASSED
    t.setheading(270) #TURN 270 DEGREES TO HEAD DOWN/SOUTH
    t.forward(height) #DRAW LINE AS LONG AS HEIGHT ARGUMENT PASSED
    t.up() #MOVE PEN TO UP POSTION TO NO LONGER DRAW
    t.end_fill() #END FILL COLORING
    
#USE A WHILE TRUE LOOP TO KEEP THE TURTLE WINDOW OPEN
while True:
    #CREATE YOUR TURTLE OBJECT TO OPEN THE DRAWING WINDOW
    t = Turtle()
    t.hideturtle()
    #GET WIDTH AND HEIGHT OF BUTTON FROM USER:
    width = int(input("Enter how many pixels wide the button will be: "))
    height = int(input("Enter how many pixels tall the button will be: "))
    #GET COLOR TO USE FOR STROKE OF SHAPE:
    stroke = str(input("Enter a color the outline of the button will be: "))
    #GET COLOR TO USE FOR FILL OF SHAPE:
    fill = str(input("Enter a color the fill of the button will be: "))
    #GET X & Y COORDINATES FOR BOTTOM-LEFT CORNER WHERE DRAWING WILL BEGIN:
    coordinates = [] #USE A LIST
    x = int(input("Enter the 'x' coordinate of where bottom left of drawing will begin: "))
    coordinates.append(x)
    y = int(input("Enter the 'y' coordinate for where bottom left of drawing will begin: "))
    coordinates.append(y)
    tuple(coordinates) #CAST LIST AS A TUPLE
    #CALL THE DRAWBUTTON FUNCTION, PASS IN THE T, WIDTH, HEIGHT, STROKE, FILL, AND COORDINATES:
    drawButton(t, width, height, stroke, fill, coordinates)
    