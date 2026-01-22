def print_numbers(n):
    for i in range(n):
        print(i)
print_numbers(3)
def check_voltages(voltages):
    for v in voltages:
        if v >= 3.3:
            print(v, "high")
        else:
            print(v,"low")
values = [3.1, 3.3, 3.8, 2.9]
check_voltages(values)
