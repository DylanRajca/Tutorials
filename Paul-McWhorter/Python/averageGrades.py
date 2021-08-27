# Tutorial 11: Finding high and low numbers in a list

# Ask user for number of grades / individual grades
# Put grades into array
# Average grades and print out average / all grades

gradeCount = int(input('How many grades do you have? '))

gradeList = []

# Initialize lowGrade to 100 and highGrade to 0, so that it is guaranteed we will find
# a grade lower/higher than our initial value.
lowGrade = 100
highGrade = 0

for i in range(1, (gradeCount + 1)):
  grade = float(input(f'Enter grade {i}: '))
  gradeList.append(grade)
  
print('\nYour grades are: ')
for grade in gradeList:
  print(grade)
  
# Find average of grades
average = float((sum(gradeList) / gradeCount))
print(f'\nThe grade average is: {average}')

# Iterate through gradeList to find high/low grades
for i in range(0, gradeCount, 1):
  if gradeList[i] < lowGrade:
    lowGrade = gradeList[i]
print('Your low grade is: ', lowGrade)

for i in range(0, gradeCount,1):
  if gradeList[i] > highGrade:
    highGrade = gradeList[i]
print('Your high grade is: ', highGrade)