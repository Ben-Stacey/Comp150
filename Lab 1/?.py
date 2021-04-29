saying = "Be as happy as possible"

print(saying[0:2])
print(saying[6:11])
print(saying)
print(saying[0:14] + " humanly " + saying[15:24])
print("The number of letters in saying is: " + str(len(saying)))

def on_many_lines(x):
    for the in x:
        print(the)
    
on_many_lines("banana")

saying = "Be as happy as possible"
print(saying.swapcase())
print(saying.upper())
print(saying.count("e"))
print(saying[0].isupper())
print(saying[:2].isalpha())

prefixes = "JKLMNOPQ"
suffix = "ack"
for letter in prefixes:
    if letter == "O":
        print("Ouack")
    elif letter == "Q":
        print("Quack")
    print(letter + suffix)
    
def count_letters(word, n):
    count = 0
    for char in word:
        if char == n:
            count+= 1
        print(count)
        
count_letters("banana", "n")
count_letters("fruit fly", "f")



def binary_string(s):
    for i in range(len((s))):
        if i == "a":
            return 1
        elif i == "e":
            return 1
        elif i == "i":
            return 1
        elif i == "o":
            return 1
        elif i == "u":
            return 1   
        else:
            return 0
    
string = "Hello World"
print(binary_string(string))

