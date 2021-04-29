# this = ["I", "am", "not", "a", "crook"]
# that = ["I", "am", "not", "a", "crook"]
# print("Test 1: {}".format(id(this) == id(that)))
# that = this
# print("Test 2: {}".format(id(this) == id(that)))
# 
# def add_lists(a, b):
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

# def print_names(name_list):
#     """
#     >>> print_names(["Brown",["Bob","Betty"],"Green",["Geoff","Gemma","Gail"]])
#     Bob Brown
#     Betty Brown
#     Geoff Green
#     Gemma Green
#     Gail Green
#     >>> print_names(["Carter",["Cathy"],"Downer",["Don"]])
#     Cathy Carter
#     Don Downer
#     """
#     result = ''
#     for i in range(len(name_list)):
#         if i % 2 != 0:
#             for item in range(len(name_list[i])):
#                 result += name_list[i][item] + ' ' + name_list[i-1] + '\n'
#     return result
#     
# print(print_names(["Brown",["Bob","Betty"],"Green",["Geoff","Gemma","Gail"]]))
# print(print_names(["Carter",["Cathy"],"Downer",["Don"]]))
# 
# def return_names(name_list):
#     """
#     >>> return_names(["Brown",["Bob","Betty"],"Green",["Geoff","Gemma","Gail"]])
#     ['Bob Brown', 'Betty Brown', 'Geoff Green', 'Gemma Green', 'Gail Green']
#     >>> return_names(["Carter",["Cathy"],"Downer",["Don"]])
#     ['Cathy Carter', 'Don Downer']
#     """
#     result = []
#     for i in range(len(name_list)):
#         if i % 2 != 0:
#             for item in range(len(name_list[i])):
#                 result += [name_list[i][item] + ' ' + name_list[i-1]]
#     return result
# 
# print(return_names(["Brown",["Bob","Betty"],"Green",["Geoff","Gemma","Gail"]]))
# print(return_names(["Carter",["Cathy"],"Downer",["Don"]]))

# def myreplace(s, old, new):
#     """
#     >>> myreplace("Mississippi", "i", "I")
#     'MIssIssippI'
#     >>> s = "I love spom!  Spom is my favorite food.  Spom, spom, spom, yum!"
#     >>> myreplace(s, "om", "am")
#     'I love spam!  Spam is my favorite food.  Spam, spam, spam, yum!'
#     """
#     x = s.replace(old, new)
#     return x
#     
# s = "I love spom!  Spom is my favorite food.  Spom, spom, spom, yum!"
#    
# print(myreplace("Mississippi", "i", "I"))
# print(myreplace(s, "om", "am"))

def zeros(n,m):
    """
    Return an n by m matrix of zeros. Each element should be unique.
    >>> A = zeros(3,2)
    >>> A
    [[0, 0], [0, 0], [0, 0]]
    >>> A[0][1] = 1
    >>> A
    [[0, 1], [0, 0], [0, 0]]
    """
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(j)
    return matrix

print(zeros(3,2))

# 
# if __name__=="__main__":
#     import doctest
#     doctest.testmod(verbose=True)