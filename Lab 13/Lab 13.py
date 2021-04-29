# def list1(x):
#     y = x[4]
#     print(y)
#     
# list1([1,2,3,4,5,6])

# def list2(x):
#     y = x[-2:]
#     print(y)
#     
# list2([1,2,3,4,5,6])

# def list3(x):
#     y = x[::2]
#     print(y)
#  
# list3([1,2,3,4,5,6])

# result = ''
# l = ["spam!", [1], ["Brie", "Roquefort", "Pol le Veq"], [1, 2, 3]]
# for i in l:
#      result += str(len(i)) + ' '
# print(result)

# def add_lists(a, b):
#     """
#     >>> add_lists([1, 1], [1, 1])
#     [2, 2]
#     >>> add_lists([1, 2], [1, 4])
#     [2, 6]
#     >>> add_lists([1, 2, 1], [1, 4, 3])
#     [2, 6, 4]
#     >>> list1 = [1, 2, 1]
#     >>> list2 = [1, 4, 3]
#     >>> sum = add_lists(list1, list2)
#     >>> list1 == [1, 2, 1]
#     True
#     >>> list2 == [1, 4, 3]
#     True
#     """
#     for i in range(len(a)):
#         a[i] += b[i]
#     return a
# 
# list1 = [1,2,3]
# list2 = [3,4,6]
# list3 = add_lists(list1, list2)
# print(list1)
# print(list2)
# print(list3)

def mult_lists(a, b):
    """
    >>> mult_lists([1, 1], [1, 1])
    2
    >>> mult_lists([1, 2], [1, 4])
    9
    >>> mult_lists([1, 2, 1], [1, 4, 3])
    12
    """
    index = 0
    count = 0
    y = 0
    while index < len(a):
        x = a[count] * b[count]
        count += 1
        index += 1
        y = x + x
    return y
    
# print(mult_lists([1, 1], [1, 1]))
print(mult_lists([1, 2], [1, 4]))
print(mult_lists([1, 2, 1], [1, 4, 3]))

# if __name__ == "__main__":
#     import doctest
#     doctest.testmod(verbose=True)