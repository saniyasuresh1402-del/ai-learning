def find_average(numbers):
    total = 0
    for n in numbers:
        total = total + n
        return total / len(numbers)
marks = [80, 65, 90, 72]
avg = find_average(marks)
print("average marks: ", avg)
