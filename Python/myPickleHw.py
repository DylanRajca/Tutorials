'''
Write 2 programs
In program 1:
  - Ask user to input number of students
  - For each student ask their name, then as their grade
  - Once all names and grades have been input, pickle data to hard drive
  
In program 2:
  - Read pickled data from hard drive
  - Ask user what student they would like the grade for
  - Read grade back to student
'''

class Student:
  def __init__(self, name, grade):
    self._name = name
    self._grade = grade
  
  def getName(self):
    return self._name
  
  def getGrade(self):
    return self._grade
  

def pickleData ():
  studentCount = int(input('How many students are there?'))
  pass
  
  

def readData ():
  pass

test = Student('dylan', 80)

print(test.getGrade())