myfile = open("a.txt", mode = "w")
myfile.write("I have a bunch of red roses")
myfile.close()
myfile = open("b.txt", mode = "w")
myfile.write("The man")
myfile.close()

def longer(x,y):
    myfile = open("a.txt", mode = "r")
    myfile = open("b.txt", mode = "r")
    a = len(x)
    b = len(y)
    if a > b:
        print(str(x) + " is longer")
    else:
        print(str(y) + " is longer")
    
one = input("a.txt")
two = input("b.txt")
longer(one, two)



