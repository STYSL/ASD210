"""
CIAT Class: ASD210 Fundamentals of Python - First Programs
STUDENT: Felicito A. Rustique
INSTRUCTOR: Nathan Kilgore
Assignment: Week 4 Programming Challenge
Task to Accomplish:
A button to change the color of the label text
"""

from breezypythongui import EasyFrame

#OTHER IMPORTS:
from tkinter.font import Font
import tkinter.colorchooser

#ButtonDemo CLASS EXTENDS EASYFRAME PARENT CLASS:
class ButtonGUI(EasyFrame):
    """Illustrates command buttons and user events.""" 
    
    def __init__(self):
        """Sets up the window, label, and buttons."""  
        EasyFrame.__init__(self, height = 480, width = 600)
          
        #A single label in the first row.  
        self.label = self.addLabel(text = "Hello world!",  row = 0, column = 0, columnspan = 3,  font = ('Impact', 80), foreground = "black", sticky = "NSEW")  
        
        #THREE command buttons in the second row, with event  
        #handler methods specified.  
        self.clearBtn = self.addButton(text = "Clear",  row = 1, column = 0, command = self.clear)
        #ADD BUTTON TO CHANGE COLOR WITH CHANGECOLOR METHOD:
        self.changeColorBtn = self.addButton(text = "Change Text Color", row = 1, column = 1, command = self.changeColor)
        self.restoreBtn = self.addButton(text = "Restore", row = 1, column = 2, state = "disabled",  command = self.restore)

        self.r = self.addIntegerField(value = 0, row = 2, column = 1, width = 6, columnspan = 1, sticky = "N")
        self.b = self.addIntegerField(value = 0, row = 2, column = 1, width = 6, columnspan = 1, sticky = "N")  
        self.g = self.addIntegerField(value = 0, row = 2, column = 1, width = 6, columnspan = 1, sticky = "N") 
        self.hex = self.addTextField(text = "", row = 2, column = 1, width = 6, columnspan = 1, sticky = "N")  
   
    #Methods to handle user events.  
    def clear(self):  
        """Resets the label to the empty string and updates the button states."""  
        self.label["text"] =  ""  
        self.clearBtn["state"] = "disabled"  
        self.restoreBtn["state"] = "normal"  

    def changeColor(self):
        """Change the color of the label text"""
        colorTuple = tkinter.colorchooser.askcolor()  
        if not colorTuple[0]: return  
        ((r, g, b), hexString) = colorTuple  
        self.r.setNumber(int(r))  
        self.g.setNumber(int(g))  
        self.b.setNumber(int(b))  
        self.hex.setText(hexString)  
        self.label["foreground"] = hexString 
                
    def restore(self):  
        """Resets the label to 'Hello world!' and updates the button states."""  
        self.label["text"] = "Hello world!"  
        self.clearBtn["state"] = "normal"  
        self.restoreBtn["state"] = "disabled" 
        
def main():
        """Instantiates and pops up the window."""
        #Application/Class Name().mainloop() 
        ButtonGUI().mainloop()
        
if __name__ == "__main__":
        main()

