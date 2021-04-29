myfile1 = open("a.txt", mode = "w")
myfile1.write("I have a bunch of red roses")
myfile1.close()
myfile2 = open("b.txt", mode = "w")
myfile2.write("The man")
myfile2.close()

myfile1 = open("a.txt", mode = "r")
myfile2 = open("b.txt", mode = "r")
a = myfile1.read()
b = myfile2.read()
if len(a) >  len(b):
    print(a)
else:
    print(b)
   



