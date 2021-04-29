def replace(s):
    f1 = open("c.txt", mode = "r")
    word = f1.read().split()
    result = ''
    for word in x:
        if word in 'aeiou':
            
            for ch in word:
                if ch.isalnum():
                    result += ch
    return x
        
print(replace('_'))