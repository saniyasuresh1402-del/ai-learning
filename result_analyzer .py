name = input("Enter student name: ")

marks = []
for i in range(5):
    m = int(input(f"Enter mark {i+1}: "))
    marks.append(m)

total = sum(marks)
average = total / len(marks)

if average >= 75:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "Fail"

print("\n--- Result ---")
print("Name:", name)
print("Marks:", marks)
print("Average:", average)
print("Grade:", grade)