def check_number(num):
    if num > 0:
        return "positive"
    elif num < 0:
        return "negative"
    else:
        return "zero"
for i in [-2, 0, 5]:
    print(i,"-", check_number(i))