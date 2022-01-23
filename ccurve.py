"""
CIAT Class: ASD210 Fundamentals of Python - First Programs
STUDENT: Felicito A. Rustique
INSTRUCTOR: Nathan Kilgore
ASSIGNMENT: Week3 Part1 Discussion.
File: ccurve.py
Project 7.2  Draws the line segments in random colors.
"""

from turtle import Turtle, tracer, update, Screen
from random import randint

#import os to use clearConsole method:
import os
#clearConsole clears screen output
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
clearConsole()

def cCurve(t, x1, y1, x2, y2, level):
   #Draws a c-curve of the given level
   
   def drawLine(x1, y1, x2, y2):
      """Draws a line segment between the endpoints,
      using a random color."""
      t.up()
      t.goto(x1, y1)
      t.down()
      t.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
      t.goto(x2, y2)
      
   if level == 0:
      drawLine(x1, y1, x2, y2)
   else:
      xm = (x1 + x2 + y1 - y2) // 2
      ym = (x2 + y1 + y2 - x1) // 2
      cCurve(t, x1, y1, xm, ym, level - 1)
      cCurve(t, xm, ym, x2, y2, level - 1)

def main():
   while True: 
      level = int(input("Enter the level (0 or greater): "))
      t = Turtle()
      #CREATE SCREEN OBJECT AND SET COLORMODE IN ORDER FOR RANDOMINT TO WORK FOR RGB VALUES:
      screen = Screen()
      screen.colormode(255)
      if level > 8:
         tracer(False)
      t.hideturtle()
      cCurve(t, 50, -50, 50, 50, level)
      if level > 8:
         update()

if __name__ == "__main__":
   main()



