def area_of_circle(radius):
    if radius < 0:
        print("Warning: radius must be non-negative")
        return
    
    area = 3.14159 * radius**2
    return area