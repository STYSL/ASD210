"""
CIAT Class:  ASD210 Fundamentals of Python - First Programs
STUDENT: Felicito A. Rustique
INSTRUCTOR: Nathan Kilgore
ASSIGNMENT: Week3 Part2 HandsOn, Project 7.5

Complete Project 7.5: Define and test a function named posterize. This function expects an image and a tuple of RGB values as arguments. 
The function modifies the image like the blackAndWhite function, but it uses the given RGB values instead of black
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

#DEFINE POSTERIZE FUNCTION:
def posterize(imageClone):
    #USE A NESTED LOOP FOR A ROW-MAJOR TRAVERSAL OF ENTIRE IMAGE GRID:
    whitePixel = (255, 255, 255)
    for y in range(imageClone.getHeight()):
        for x in range(imageClone.getWidth()):
            (r, g, b) = imageClone.getPixel(x, y)
            average = (r + g + b) // 3
            if average < 128:
                imageClone.setPixel(x, y, (r,g,b))
            else:
                imageClone.setPixel(x,y, whitePixel)
    
#USE A WHILE TRUE LOOP TO KEEP THE TURTLE WINDOW OPEN
def main(filename = "smokey.gif"):
    #CREATE IMAGE OBJECT SET TO SMOKEY.GIF:
    image = Image("smokey.gif")
    #MAKE A COPY/CLONE OF THE IMAGE TO PREVENT SAVING OVER:
    imageClone = image.clone()
    print("Close the image window to continue and see a posterized version.")
    #DISPLAY THE IMAGE:
    imageClone.draw()
    #CALL THE POSTERIZE FUNCTION, PASS IN IMAGE ARGUMENT:
    posterize(imageClone)
    print("Close the image window to quit and save this posterized version as 'posterized.gif'")
    #DISPLAY THE NEW imageClone RESULT:
    imageClone.draw()
    #SAVE THE NEW imageClone RESULT:
    imageClone.save("posterized")
    
if __name__ == "__main__":
    main()
