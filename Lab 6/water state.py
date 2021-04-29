def water_state(temp):
    if temp > 100:
        return"Steam"
    elif temp < 0:
        return "Ice"
    else:
        return "Liquid"
        
temp = input("State a tempreture: " )
print("H20 at " + temp + " degrees will be steam")
