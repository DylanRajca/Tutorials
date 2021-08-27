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
import pickle

def userInput():
    studentCount = int(input("How many students are there? "))
    studentGrades = {}

    for i in range(1, (studentCount + 1), 1):
        student = str(input(f"Enter student {i} name: "))
        age = int(input(f"Enter student {i} grade: "))
        studentGrades[student] = age

    # Pickle studentGrades as binary file
    with open('Python/myData.pkl', 'wb') as x:
        pickle.dump(studentGrades, x)


def readData():
    with open('Python/myData.pkl', 'rb') as x:
        data = pickle.load(x)
    print(data)

readData()