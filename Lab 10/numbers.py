def num_digits(n):
    """
    >>> num_digits(12345)
    5
    >>> num_digits(1)
    1
    >>> num_digits(-12345)
    5
    """
    count = 0
    if n < 0:
         n = abs(n)
    while n > 0:
        count = count + 1
        n = n // 10
    return count

print(num_digits(12345))
print(num_digits(1))
print(num_digits(-12345))


if __name__ == "__main__":
#     import doctest
#     doctest.testmod(verbose=True)
    numfile = open("numbers.txt")
    line = numfile.readline()
    while line:
        print(line, end='')
        line = numfile.readline()
    numfile.close()
