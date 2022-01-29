"""
CIAT Class:  ASD210 Fundamentals of Python - First Programs
STUDENT: Felicito A. Rustique
INSTRUCTOR: Nathan Kilgore
ASSIGNMENT: Week 4 Part 1, Exercise 1 | File: grayscale3.py
Task to Accomplish: Add two more images to the project
Create a loop in the main module in grayscale3.py that allow entering new image file name and/or exit
"""

#IMPORT IMAGES MODULE TO USE IMAGE CLASS
from images import Image

#import os to use clearConsole method:
import os
#clearConsole clears screen output
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
clearConsole()

def grayscale1(image):
    """Converts an image to grayscale using the
    psychologically accurate transformations."""
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            r = int(r * 0.299)
            g = int(g * 0.587)
            b = int(b * 0.114)
            lum = r + g + b
            image.setPixel(x, y, (lum, lum, lum))

def grayscale2(image):
    """Converts an image to grayscale using the crude average
    of the r, g, and b"""
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            ave = (r + g + b) // 3
            image.setPixel(x, y, (ave, ave, ave))

def main():
    print("\nThis program lets you see the grayscale version of up to 3 images in your current directory.")
    for image in range(3):
        try:
            image = input("\nEnter image file name or 'q' to quit: ")
            if image.lower() == "q":
                break
            image = Image(f"{image}")
            grayscale1(image)
            print("Close image window to enter next image.")
            image.draw()
        except Exception as e:
            e = "Invalid entry or nothing found. Try again"
            print(e)
    print("\nThree images were displayed, or you quit. Good-Bye.\n")
            
if __name__ == "__main__":
   main()


