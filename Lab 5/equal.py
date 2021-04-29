def equal(x, y, z):
    if x == y and y == z:
        print("All inputs are equal")
    elif x == y or x == z or z == y:
        print("Two inputs are the same")
    else:
        print("No inputs match")
    
equal(1, 2, 3)
equal(1, 1, 2)
equal(1, 1, 1)