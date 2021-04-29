def binary_string(input_str):
    result = ''
    for ch in input_str:
        if ch == "a":
            result += '1'
        elif ch == "e":
            result += '1'
        elif ch == "i":
            result += '1'
        elif ch == "o":
            result += '1'
        elif ch == "u":
            result += '1'  
        else:
            result += '0'
    return result

saying = "Hello World"
print(binary_string(saying))