def remove_duplicates(string):
    result = "".join(dict.fromkeys(string))
    return result

print(remove_duplicates("apple"))
print(remove_duplicates("Mississippi"))
print(remove_duplicates("The quick brown fox jumps over the lazy dog"))