# def upper_lower_swap(string):
#     """
#     >>> upper_lower_swap("The rain in Spain")
#     'tHE RAIN IN sPAIN'
#     >>> upper_lower_swap("LaTeX is better than MSWord")
#     'lAtEx IS BETTER THAN mswORD'
#     """
#     string = string.swapcase()
#     return string
# 
# print(upper_lower_swap("The rain in Spain"))
# print(upper_lower_swap("LaTeX is better than MSWord"))

# def count_appluses(filename):
#     wordfile = open(filename)
#     wordfile = wordfile.read()
#     x = range(90, 100)
#     for i in x:
#         return i
#     
# print(count_appluses('id_file.txt'))

def count_bigrams(instring, bigram):
    """
    >>> count_bigrams('A bigram is not a trigram', 'ig')
    2
    >>> count_bigrams('A bigram is not a trigram', 'am')
    2
    >>> count_bigrams('Can anyone see any cantanas?', 'an')
    5
    >>> count_bigrams('Can anyone see any cantanas?', 'es')
    0
    """
    count = 0
    b = bigram[0]
    g = bigram[1]
    for ch in instring:
        if ch is b and g == g:
            count += 1
    return count
    

print(count_bigrams('A bigram is not a trigram', 'ig'))
print(count_bigrams('A bigram is not a trigram', 'am'))
print(count_bigrams('Can anyone see any cantanas?', 'an'))
print(count_bigrams('Can anyone see any cantanas?', 'es'))



# if __name__ == "__main__":
#     import doctest
#     doctest.testmod(verbose=True)