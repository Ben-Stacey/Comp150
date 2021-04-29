def area_of_circle(radius):
    if radius < 0:
        print("Warning: radius must be non-negative")
    
    area = 3.14159 * int(radius)**2
    return area

def area_of_snowman(head, middle, bottom):
    return area_of_circle(head) + area_of_circle(middle) + area_of_circle(bottom)
      
print(area_of_circle(2))
print(area_of_snowman(2,3,4))
