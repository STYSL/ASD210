"""
CIAT Class: ASD210 Fundamentals of Python - First Programs
STUDENT: Felicito A. Rustique
INSTRUCTOR: Nathan Kilgore
ASSIGNMENT: Week 4 Part 2 Hands-On - Complete Project 1: 
Add three methods to the Student class that compare two Student objects.
One method should test for equality. A second method should test for less than.
The third method should test for greater than or equal to.
In each case, the method returns the result of the comparison of the two students’ names. 
Include a main function that tests all of the comparison operators.
"""

from breezypythongui import EasyFrame
import os, os.path

class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self.name
  
    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]
   
    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self._scores)
    
    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)
 
    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))

    def __eq__(self, other):
        """Tests for equality."""
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        else:
            return self.name == other.name

    def __lt__(self, other):
        """Returns self < other, with respect to names."""
        return self.name < other.name 

    def __ge__(self, other):
        """Returns self >= other, with respect
        to names."""
        return self.name >= other.name 

def main():
    """Instatiate student objects of the type Student class."""
    student1 = Student("Jack", 5)
    #SET 5 SCORES FOR STUDENT 1 TO USE FOR COMPARING:
    student1.setScore(1, 100)
    student1.setScore(2, 90)
    student1.setScore(3, 85)
    student1.setScore(4, 75)
    student1.setScore(5, 100)
    print(f"\nStudent {student1}")
    #WE'RE NOT GOING TO SET ALL STUDENT'S SCORES TO 100:
    #for i in range(1, 6):
    #    student1.setScore(i, 100)
    #print(student1)

    #CREATE 2ND STUDENT:
    student2 = Student("Jill", 5)
    #SET 5 SCORES FOR STUDENT 1 TO USE FOR COMPARING:
    student2.setScore(1, 100)
    student2.setScore(2, 100)
    student2.setScore(3, 95)
    student2.setScore(4, 65)
    student2.setScore(5, 80)
    print(f"\nStudent {student2}")
    #WE'RE NOT GOING TO SET ALL STUDENT'S SCORES TO 100:
    #for i in range(1, 6):
    #    student2.setScore(i, 100)
    #print(student2)
    
    print(f"""\nStudent name of {student1.getName()}
compared to student name of {student2.getName()}
is as follows: \n""")
    print(f"Equal to: ", student1 == student2)
    print(f"Less than: ", student1 < student2)
    print(f"Greater than: ", student1 > student2)
    print()

if __name__ == "__main__":
    main()



