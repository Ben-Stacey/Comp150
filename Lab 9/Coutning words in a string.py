myfile1 = open("a.txt", mode = "r")
myfile2 = open("b.txt", mode = "r")
x = myfile1.read()
y = myfile2.read()
word_list1 = x.split()
word_list2 = y.split()
if len(word_list1) > len(word_list2):
    print(x)
else:
    print(y)
