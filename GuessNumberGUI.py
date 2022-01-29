"""
CIAT Class: ASD210 Fundamentals of Python - First Programs
STUDENT: Felicito A. Rustique
INSTRUCTOR: Nathan Kilgore
ASSIGNMENT: Week 4 Part 1 Hands-On - From Pg. 291, Complete project 5: 
Write a GUI-based program that plays a guess-the-number game in which the roles of the computer 
and the user are the reverse of what they are in the Case Study of this chapter. 
In this version of the game, the computer guesses a number between 1 and 100 and the user provides the responses. 
The window should display the computer’s guesses with a label. 
The user enters a hint in response, by selecting one of a set of command buttons labeled Too small, Too large, and Correct. 
When the game is over, you should disable these buttons and wait for the user to click New game, as before. 
"""

from breezypythongui import EasyFrame
from tkinter import *
from random import randint

#PANEL GUESSNUMBER CLASS EXTENDS EASYFRAME PARENT CLASS:
class GuessNumber(EasyFrame):  
    """Computer guesses a number between 1 and 100 and the user provides the responses."""  
    
    #DEFINE THE CONSTRUCTOR:
    def __init__(self):  
        
        #CREATE THE MAIN FRAME: 
        EasyFrame.__init__(self, title = "Guess the Number", height = 150, width = 400)  
        
        self.count = 1
        
        #CREATE PROMPTER BOX TO SET NUMBER FOR COMPUTER TO GUESS:
        self.num2guess = self.prompterBox(title = "Input",  promptString = "Enter an integer between 1 and 100 for computer to guess: ")
        int(self.num2guess)
        
        #CREATE COMPUTER GUESS:
        self.computerGuess = randint(1,100)
        
        #CREATE 2 ROWS W/ LABELS & FIELDS NESTED IN THE GUESS PANEL:
        self.label1 = self.addLabel(text = "NUMBER TO GUESS:", row = 0, column =0, sticky = "E")
        self.integer1 = self.addIntegerField(value = self.num2guess, row = 0, column = 1, sticky = "NSEW")
        
        self.label2 = self.addLabel(text = "COMPUTER GUESS:", row = 1, column =0, sticky = "E")
        self.integer2 = self.addIntegerField(value = self.computerGuess, row = 1, column = 1, sticky = "NSEW", state = "readonly")
        
        self.label3 = self.addLabel(text = "GUESS COUNT:", row = 2, column =0, sticky = "E")
        self.integer3 = self.addIntegerField(value = self.count, row = 2, column = 1, sticky = "NSEW", state = "readonly")
        
        #CREATE THE BUTTON PANEL TO HOLD TWO ROWS
        buttonPanel = self.addPanel(row = 3, column = 0,  background = "black", columnspan = 2)  
        
        #FIRST ROW FOR TOO SMALL, TOO LARGE AND CORRECT BUTTONS.
        #ADD COMMMAND ATTRIBUTES TO TRIGGER EVENT HANDLING METHODS:
        self.button1 = buttonPanel.addButton(text = "Too Small", row = 0, column = 0, command = self.tooSmall)  
        self.button2 = buttonPanel.addButton(text = "Too Large", row = 0, column = 1, command = self.tooLarge)  
        self.button3 = buttonPanel.addButton(text = "Correct!", row = 0, column = 2, command = self.correct) 

        #SECOND ROW FOR NEW GAME BUTTON
        self.button4 = buttonPanel.addButton(text = "New Game", row = 1, column = 0, columnspan= 3, command = self.newGame) 

 
    #EVENT HANDLING METHODS FOR BUTTONS:
    def tooSmall(self):
        """Generates a new number that's larger than the previous computer's guess"""
        self.count += 1
        self.computerGuess = randint(self.computerGuess, 100)
        #INSERT NEW VALUES BACK INTO GUI:
        self.integer2 = self.addIntegerField(value = self.computerGuess, row = 1, column = 1, sticky = "NSEW", state = "readonly")
        self.integer3 = self.addIntegerField(value = self.count, row = 2, column = 1, sticky = "NSEW", state = "readonly")
        print(self.computerGuess) #FOR TERMINAL TO SHOW METHOD WORKS

    
    def tooLarge(self):
        """Generates a new number that's smaller than the previous computer's guess"""
        self.count += 1
        self.computerGuess = randint(1, self.computerGuess)
        #INSERT NEW VALUES BACK INTO GUI:
        self.integer2 = self.addIntegerField(value = self.computerGuess, row = 1, column = 1, sticky = "NSEW", state = "readonly")
        self.integer3 = self.addIntegerField(value = self.count, row = 2, column = 1, sticky = "NSEW", state = "readonly")
        print(self.computerGuess) #FOR TERMINAL TO SHOW METHOD WORKS
    
    def correct(self):
        """Disables too small and too large buttons when clicked"""
        self.button1["state"] = "disabled"
        self.button2["state"] = "disabled"  

    def newGame(self):
        """Resets the data and GUI to their original states."""
        main()
        
#DEFINE THE MAIN FUNCTION:    
def main():
        """Instantiates and pops up the window."""
        GuessNumber().mainloop()

#TRIGGER THE MAIN FUNCTION:        
if __name__ == "__main__":
        main()
