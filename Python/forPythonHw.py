# Ask user for number of grades / individual grades
# Put grades into array
# Average grades and print out average / all grades

gradeCount = int(input('How many grades do you have? '))

gradeList = []

for i in range(1, (gradeCount + 1)):
  grade = float(input(f'Enter grade {i}: '))
  gradeList.append(grade)
  
average = (sum(gradeList) / gradeCount)

print(f'The grade average is: {average}')
print('Your grades are: ')

for grade in gradeList:
  print(grade)