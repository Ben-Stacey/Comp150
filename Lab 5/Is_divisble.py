def is_divisible_by_3(x):
    if x % 3:
        print("This number is not divisble by three.")
    else:
        print("This number is divisble by three.")
              
x = input("Enter a number: ")
is_divisible_by_3(int(x))

def is_divisible_by_5(x):
    if x % 5:
        print("This number is not divisble by five.")
    else:
        print("This number is divisble by five.")
              
x = input("Enter a number: ")
is_divisible_by_5(int(x))

def is_divisible(x,y):
    if x % y:
        print(x, " is not divisible by ", y)
    else:
        print(x, " is divisible by ", y)

is_divisible(6,2)
    