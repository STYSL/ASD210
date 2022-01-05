"""
CIAT Class:  ASD210 Fundamentals of Python - First Programs
STUDENT: Felicito A. Rustique
INSTRUCTOR: Nathan Kilgore
ASSIGNMENT: Week1 Part1 HandsOn
"""

from math import pi

#import os to use clearConsole method:
import os

#clearConsole clears screen output
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

clearConsole()

#From Pg. 33 of the text:
"""
Complete project 2: Write a Python program that prints (displays) your name, address, and telephone number. 
"""
print("Name: Felicito A. Rustique Jr \n Address: 1234 Sesame Street \n Phone Number: 1-800-YOU-CODE")
print("")

"""
Complete project 6: Write and test a program that computes the area of a circle. This program should request a number representing a radius as input from the user. It should use the formula  3.14 * radius ** 2 to compute the area and then output this result suitably labeled. 
"""

circleRadius = float(input("Enter the radius of your circle: "))
area = 3.14 * circleRadius **2
print("The radius of your cirlce is: ", area)
print("")

"""
Complete project 7: Write and test a program that accepts the user’s name (as text) and age (as a number)  as input. The program should output a sentence containing the user’s name and age. 
"""

name = str(input("Enter your name: "))
age = int(input("Enter your age in whole years: "))
print("Your name is " + name + " and your age is ", age)
print("")

#From Pg. 62 of the text:
"""
Complete project 2: Write a program that takes the length of an edge (an integer) as input and prints the cube’s surface area as output. 
"""

cubeEdgeLength = int(input("Enter the length of one of the edges of your cube, rounded to the nearest whole number: "))
surfaceArea = (cubeEdgeLength **2) * 6
#Alternate way using pow function from math library:  
#surfaceArea = pow(cubeEdgeLength,2) * 6
print("The total surface area of your cube is: ", surfaceArea)
print("")

"""
Complete project 4: Write a program that takes the radius of a sphere (a floating-point number) as input and then outputs the sphere’s diameter, circumference, surface area, and volume.
"""

sphereRadius = float(input("Enter the radius of your sphere: "))
diameter = sphereRadius * 2
circumference = 2 * pi * sphereRadius
surfaceArea = 4 * pi * sphereRadius **2
volume = 4/3 * pi * sphereRadius **3
print("The diameter of your sphere is: ", diameter)
print("The circumference of your sphere is: ", circumference)
print("The surface area of your sphere is: ", surfaceArea)
print("The volume of your sphere is: ", volume)
print("")