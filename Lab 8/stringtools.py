def remove_letter(letter, string):
    result = ""
    for ch in string:
        if ch.replace(letter, ""):
            result += ch
    return result

def reverse(s):
    return s[::-1]

def mirror(s):
    result = ""
    result += s
    result += s[::-1]
    return result
    
print(mirror("good"))
print(mirror("yes"))
print(mirror("Python"))
print(mirror(""))
print(mirror("a"))
print(reverse("happy"))
print(reverse("Python"))
print(reverse(""))
print(reverse("P"))
print(remove_letter('a', 'apple'))
print(remove_letter('a','banana'))
print(remove_letter('z', 'banana'))
print(remove_letter('i', 'mississippi'))

