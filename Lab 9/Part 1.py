import os
dir_list = os.listdir()
print(dir_list)
myfile = open("test.txt", mode = "w")
myfile.write("I have a bunch/nof red roses/n")
myfile.close()
myfile = open("test.txt", mode = "r")
line = myfile.read()
print(line)

def one_line(myfile):
    myfile = open("test.txt", mode = "r")
    line = myfile.read()
    new = line.replace("/n", "_")
    print(new)
        
one_line("text.txt")

def find_int(myfile, x):
    myfile = open("test.txt", mode = "r")
    line = myfile.read(x)
    print(line)

find_int("text.txt", 1)
find_int("text.txt", 0)

def find_word(myfile, s):
    myfile = open("test.txt", mode = "r")
    line = myfile.read()
    if s in line:
        print(True)
    else:
        print(False)
        
find_word("text.txt", "have")
find_word("rext.txt", "the")

def target(myfile, s1, s2):
    myfile = open("test.txt", mode = "r")
    line = myfile.read()
    if s1 in line and s2 in line:
        print(True)
    else:
        print(False)
    
target("text.txt", "I", "a")
target("text.txt", "i", "a")
target("text.txt", "you", "a")

