import math
    
def is_even(n):
    if n % 2:
        return "False"
    else:
        return "True"

def is_odd(n):
    if n % 2:
        return "True"
    else:
        return "False"
    
def is_factor(x,y):
    if x % y == 0:
        return "True"
    else:
        return "False"
    
def hypotenuse(a,b):
    return math.sqrt(pow(a,2) + pow(b,2))

print(is_even(5))
print(is_odd(5))
print(is_factor(3,12))
print(is_factor(5,12))
print(hypotenuse(3,4))
    

