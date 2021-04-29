def only_upper(input_str):
    result = ''
    for ch in input_str:
        if ch.isupper():
            result += ch
    return result
    
saying = "Be As Happy As Possible"
print(only_upper(saying))