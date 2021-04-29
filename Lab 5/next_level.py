def next_level(x, y, z, a, b, c):
    score = (x + y + z + a + b + c) - (min(x, y, z, a, b, c))
    if score >= 200:
        return "pass"
    else:
        return "repeat"
        
print(next_level(1, 2, 3, 4, 5, 6))
print(next_level(40,40,40,40,40,30))