def scrabble_score(input_str):
    count = 0
    for ch in input_str:
        if ch == 'E' or ch == 'A' or ch == 'I' or ch == 'O' or ch == 'N' or ch == 'R' or ch == 'T' or ch == 'L' or ch == 'S' or ch == 'U':
            count += 1
        elif ch == 'D' or ch == 'G':
            count += 2
        elif ch == 'B' or ch == 'C' or ch == 'M' or ch == 'P':
            count += 3
        elif ch == 'F' or ch == 'H' or ch == 'V' or ch == 'W' or ch == 'Y':
            count += 4
        elif ch == 'K':
            count += 5
        elif ch == 'J' or ch == 'X':
            count += 8
        elif ch == 'Q' or ch == ' Z':
            count += 10
    return count
    
saying = "AABBWOL"
print(scrabble_score(saying))