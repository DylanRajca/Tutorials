'''
Tutorial 11: Finding high and low numbers in a list
Ask user for number of grades / individual grades
Put grades into array
Average grades and print out average / all grades

HW: sort gradesList from high to low and print new list
'''

gradeCount = int(input('How many grades do you have? '))
gradeList = []
sortedGradeList = []

# Initialize lowGrade to 100 and highGrade to 0, so that it is guaranteed we will find
# a grade lower/higher than our initial value.
lowGrade = 100
highGrade = 0

# Ask user to input grades and append to gradeList
for i in range(1, (gradeCount + 1)):
    grade = float(input(f'Enter grade {i}: '))
    gradeList.append(grade)

# Sort grades from high to low and insert into sortedGradeList
for i in range(0, (gradeCount - 1), 1):
    for i in range(0, (gradeCount - 1), 1):
        if gradeList[i] < gradeList[i + 1]:
            swap = gradeList[i]
            gradeList[i] = gradeList[i + 1]
            gradeList[i + 1] = swap

# Print ordered list of grades
print('\nYour sorted grade list is: ')
for grade in gradeList:
    print(grade)

# Add gradeList and find average of grades
sum = 0
for i in range(0, gradeCount, 1):
    sum = sum + gradeList[i]
average = float(sum / gradeCount)
print(f'\nThe grade average is: {average}')

# Iterate through gradeList to find high/low grades
for i in range(0, gradeCount, 1):
    if gradeList[i] < lowGrade:
        lowGrade = gradeList[i]
    if gradeList[i] > highGrade:
        highGrade = gradeList[i]
print('Your low grade is: ', lowGrade)
print('Your high grade is: ', highGrade)
