import sys

if len(sys.argv) == 6:
    script_name = sys.argv[0]
    marks = [float(m) for m in sys.argv[1:6]]
    print("User provided marks values:")
else:
    script_name = sys.argv[0]
    marks = [80, 75, 90, 85, 70]
    print("No input given - using default marks:")

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
