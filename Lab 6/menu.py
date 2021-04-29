def triangle():
    l = input("Enter the length: ")
    h = input("Enter the height: ")
    print((int(l)*int(h))/0.5)
    
def circle():
    r = input("Enter the radius: ")
    print(3.14159*int(r)**2)

def square ():
    x = input("Enter the length: ")
    y = input("Enter the height: ")
    print(int(x)*int(y))

def menu(number):
    if number == 'triangle':
        triangle()
    elif number == 'circle':
        circle()
    elif number == 'square':
        square()
    else:
        print("Enter a number between 1 and 3")
        
print("Calculate the area of which shape?")
print("triangle")
print("circle")
print("square")
number = input("Enter a number to choose: ")
menu(number)
