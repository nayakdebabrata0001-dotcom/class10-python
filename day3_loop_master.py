print("=== SE Grade Calculator Day 3 ===")

total_subjects = int(input("How many subjects? "))
total_marks = 0

for i in range(total_subjects):
    marks = int(input(f"Enter marks for subject {i+1}: "))
    total_marks = total_marks + marks

average = total_marks / total_subjects
print("Total:", total_marks)
print("Average:", average)

if average >= 90:
    print("Grade: A - SE material bhai!")
elif average >= 75:
    print("Grade: B - Keep grinding")
elif average >= 60:
    print("Grade: C - Push harder")
else:
    print("Grade: D - Debug your study plan")
