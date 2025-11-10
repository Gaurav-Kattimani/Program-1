marks = [85, 78, 92, 67, 74]  
average = sum(marks) / len(marks)

if average >= 85:
    grade = 'A'
elif average >= 70:
    grade = 'B'
elif average >= 55:
    grade = 'C'
elif average >= 40:
    grade = 'D'
else:
    grade = 'Fail'

print(f"Marks: {marks}")
print(f"Average Marks: {average:.2f}")
print(f"Grade: {grade}")