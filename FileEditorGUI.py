"""
CIAT Class: ASD210 Fundamentals of Python - First Programs
STUDENT: Felicito A. Rustique
INSTRUCTOR: Nathan Kilgore
ASSIGNMENT: Week 4 Part 1 Hands-On - Pg. 292, Complete project 8:
Write a GUI-based program that allows the user to open, edit, and save text files. 
The GUI should include a labeled entry field for the filename and a multiline text widget for the text of the file. 
The user should be able to scroll through the text by manipulating a vertical scrollbar. 
Include command buttons labeled  Open, Save, and New that allow the user to open, save, and create new files. 
The New command should then clear the text widget and the entry widget. 
"""

from breezypythongui import EasyFrame
import tkinter.filedialog
#import os, os.path

class FileEditor(EasyFrame):
    """A GUI-based program that allows the user to open, edit, and save text files."""
    
    def __init__(self):
         #CREATE THE MAIN FRAME: 
        EasyFrame.__init__(self, title = "Python File Editor", height = 480, width = 600)  

        #CREATE & ADD TEXT AREA, SET WRAP ATTRIBUTE TO WORD TO CREATE LINE RETURNS:
        self.outputArea = self.addTextArea("Type text here to save, or open an existing file...", row = 0, column = 0, columnspan = 3, width = 80, height = 15, wrap = "word")
        
        #CREATE THE BUTTON PANEL TO HOLD THE BUTTONS:
        buttonPanel = self.addPanel(row = 1, column = 0,  background = "black")
        self.button1 = buttonPanel.addButton(text = "New", row = 1, column = 0, command = self.newFile)
        self.button2 = buttonPanel.addButton(text = "Open", row = 1, column = 1, command = self.openFile)
        self.button3 = buttonPanel.addButton(text = "Save", row = 1, column = 2, command = self.saveFile)
        
        
    #CREATE EVENT HANDLERS:    
    def newFile(self):
        """Clears the text area and the title bar."""
        self.outputArea.setText("Type text here...")
        self.setTitle("Python File Editor")
        
    def openFile(self):
        """Opens a file dialog and if a file is selected, displays contents in the text area."""
        fList =[("Text files", "*.txt"), ("Python files", "*.py"), ("Word files", "*.docx")]
        fileName = tkinter.filedialog.askopenfilename(parent=self,filetypes=fList)
        if fileName != "":
            file = open(fileName, 'r')
            text = file.read()
            file.close()
            self.outputArea.setText(text)
            self.setTitle(fileName)
        
    def saveFile(self):
        """Opens a file dialog and if a file is selected, displays contents in the text area."""

        fList =[("Text files", "*.txt"), ("Python files", "*.py"), ("Word files", "*.docx")]
        fileName = tkinter.filedialog.asksaveasfilename(parent=self,filetypes=fList)
        
        if fileName !="":
            file=open(fileName,'w')
            file.write(self.outputArea.getText())
            file.close()
            self.setTitle(fileName)
        
def main():
        """Instantiates and pops up the window."""
        FileEditor().mainloop()
        
if __name__ == "__main__":
        main()


