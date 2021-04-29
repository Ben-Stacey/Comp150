# def word(filename, x):
#     result = ''
#     index = 0
#     count = 0
#     wordfile = open(filename)
#     wordfile = wordfile.readline().split()
#     while index < len(wordfile):
#         if wordfile[index] == x:
#             count += 1
#             result += wordfile[index] + ' ' + str(count)
#         index += 1
#     return result
# 
# print(word('fishy.txt', 'One'))

# def numbers(filename):
#     result = ''
#     index = 0
#     wordfile = open(filename)
#     wordfile = list(str(wordfile.readline()))
#     while index < len(wordfile):
#         result += wordfile[index] + ' '
#         index += 1
#     return result
# 
# print(numbers('id_file.txt'))

def print_powers(n, high):
    result = ''
    count = 0
    while count <= high:
        result += str(count * n) + ' '
        count += 1
    print(result)


def print_powers_table(high):
    row = 1
    while row <= high:
        print_powers(row, high)
        row += 1
        
print_powers_table(3)

# def is_prime(n):
#     if n > 1:
#         for i in range(2,n):
#             if (n % i) == 0:  
#                 return 'not a prime number'
#                 break
#         else:  
#             return n

# def number_of_prime_numbers(x):
#     index = 0
#     result = ''
#     while index <= 10:
#         is_prime(x)
#         result += str(index)
#         index += 1
#     return result
#     
# print(number_of_prime_numbers(10))