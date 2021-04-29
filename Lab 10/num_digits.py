# def num_digits(n):
#     """
#     >>> num_digits(12345)
#     5
#     >>> num_digits(1)
#     1
#     >>> num_digits(-12345)
#     5
#     """
#     count = 0
#     if n < 0:
#          n = abs(n)
#     while n > 0:
#         count = count + 1
#         n = n // 10
#     return count
# 
# print(num_digits(12345))
# print(num_digits(1))
# print(num_digits(-12345))

# def num_even_digits(n):
#     """
#     >>> num_even_digits(123456)
#     3
#     >>> num_even_digits(2468)
#     4
#     >>> num_even_digits(1357)
#     0
#     >>> num_even_digits(2)
#     1
#     >>> num_even_digits(20)
#     2
#     """
#     count = 0
#     while n > 0:
#         if n % 2 == 0:
#             count = count + 1
#         n = n // 10
#     return count
# 
# print(num_even_digits(123456))
# print(num_even_digits(2468))
# print(num_even_digits(1357))
# print(num_even_digits(2))
# print(num_even_digits(20))

# def print_digits(n):
#     """
#     >>> print_digits(13789)
#     98731
#     >>> print_digits(39874613)
#     31647893
#     >>> print_digits(213141)
#     141312
#     """
#     n = str(n)
#     index = len(n) -1
#     result = ''
#     while index >= 0:
#         result += n[index]
#         index += -1 
#     return result
#         
#         
# 
# print(print_digits(13789))
# print(print_digits(39874613))
# print(print_digits(213141))
# 
# def decode(s,x):
#     """
#     >>> decode("I want no more to endure the names I am called by many people", 'n'
#     'today'
#     >>> decode("Hungry hares in lairs","r")
#     'yes'
#     >>> decode("Turn around dear","r")
#     'no'
#     """
#     index = 0
#     result = ''
#     while index < len(s)-1:
#         if s[index] == x:
#             result += s[index + 1] 
#         index += 1
#     return result
# 
# print(decode("I want no more to endure the names I am called by many people", 'n'))
# print(decode("Hungry hares in lairs","r"))
# print(decode("Turn around dear","r"))
#     
# def line_length(f, x):
#     """
#     >>> line_length("words.txt",7)
#     I have 
#     a bunch
#     of red 
#     roses
#     """
#     myfile = open(f, mode = "r")
#     line = myfile.read().replace('\n', "")
#     index = 1
#     result = line[0]
#     while index < len(line):
#         if index % x == 0:
#             result += '\n'
#         result += line[index]
#         index += 1
#     print(result)
#     
# line_length("words.txt",7)
# 
# def id_format(f):
#     """
#     >>> id_format("id_file.txt")
#     ID age year
#     123 15 2017
#     4264 25 2003
#     2014 22 1998
#     4721 16 2017
#     """
#     myfile = open(f, mode = "r")
#     line = myfile.read().replace(',', ' ')
#     print("ID age year")
#     print(line)
# 
# id_format("id_file.txt")

# def id_format3(f, x):
#     """
#     >>> id_format3("id_file2.txt",2017)
#     2
#     """
#     filename = f
#     wordfile = open(filename)
#     one_line = wordfile.readline().split()
#     count = 0
#     while one_line:
#         for word in one_line:
#             if word == str(x):
#                 count = count + 1
#         one_line = wordfile.readline().split()
#     return count
#     
# print(id_format3("id_file2.txt", 2017))

# def print_first_word(f):
#     """
#     >>> print_first_word("words.txt")
#     I of
#     """
#     filename = f
#     wordfile = open(filename)
#     one_line = wordfile.readline()
#     result = ''
#     while one_line:
#         first_word = one_line.split()[0]
#         result += first_word + ' '
#         one_line = wordfile.readline()
#     wordfile.close()
#     return result
#     
# print(print_first_word("words.txt"))

# def print_line3(f):
#     """
#     >>> print_line3("words.txt")
#     I w w w
#     of w w
#     """
#     filename = f
#     wordfile = open(filename)
#     one_line = wordfile.readline().split()
#     result = ''
#     while one_line:
#         result += one_line[0] + ' ' + 'w ' * (len(one_line) -1) + '\n'
#         one_line = wordfile.readline().split()
#     wordfile.close()
#     return result
#     
# print(print_line3("words.txt"))
# 
# def new_line(f, x):
#     filename = f
#     wordfile = open(filename)
#     one_line = wordfile.readline()
#     result = ''
#     while one_line:
#         for ch in one_line:
#             if ch == x:
#                 result = result + one_line
#         one_line = wordfile.readline()
#     return result
# 
# print(new_line("new_line.txt", 'T'))


# def compact_a(f):
#     filename = f
#     wordfile = open(filename)
#     one_line = wordfile.readline()
#     index = 0
#     result = ''
#     while one_line:
#         if index % 2 == 0:
#             result += one_line.replace('\n', '')
#         else:
#             result += one_line
#         index = index + 1 
#         one_line = wordfile.readline()
#     return result
#     
# print(compact_a("fishy.txt"))

# def compact_b(f):
#     """
#     >>> compact_b("fishy.txt")
#     'One fishTwo fish\\nRed fishBlue fish\\n'
#     """
#     filename = f
#     wordfile= open(filename)
#     one_line = wordfile.readline()
#     index = 0
#     result = ''
#     while one_line:
#         if index % 2 == 0:
#             result =  result + one_line.replace('\n', '')
#         else:
#             result = result + one_line.replace(' ', '\\n')
#         index = index + 1 
#         one_line = wordfile.readline()
#     return result
#     
# print(compact_b("fishy.txt"))


# if __name__ == "__main__":
#     import doctest
#     doctest.testmod(verbose=True)