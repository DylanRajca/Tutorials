# Tutorial 9: Understanding for loops in Python

# Prompt user for number of grades they have. 
# Ask user for grades
# Print grades out

gradeCount = int(input('How many grades do you have? '))

gradeList = []

for i in range(1, (gradeCount + 1)):
  grade = float(input(f'Enter grade {i}: '))
  gradeList.append(grade)
  
print('Your grades are: ')

for grades in gradeList:
  print(grade)