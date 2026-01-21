def check_temprature(temp):
    if temp > 30:
        return "hot"
    elif temp > 20:
        return "moderate"
    else:
        return "cold"
current = check_temprature(25)
print("tempratuer is:", current)
def voltage_status(v):
    if v >= 3.3:
        return "logic high"
    else:
        return "logic low"
status = voltage_status(3.1)
print(status)
    
    