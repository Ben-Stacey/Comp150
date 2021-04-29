import math

def compare(a,b):
    """
    Return 1 if a>b, 0 if a equals b, and -1 if a<b
    >>> compare (5,4)
    1
    >>> compare (7,7)
    0
    >>> compare (2,3)
    -1
    >>> compare (42,1)
    1
    """
    return 1

def hypotenuse(a,b):
    """
    Compute the hypotuneuse of a right triangle with sides of length a and b
    >>> hypotenuse(3,4)
    5.0
    >>> hypotenuse(12,5)
    13.0
    >>> hypotenuse(7,24)
    25.0
    >>> hypotenuse(9,12)
    15.0
    """
    return math.sqrt(a**2+b**2)

def fahrentheit_to_celsuis(n):
    """
    >>> fahrentheit_to_celsuis(0)
    32
    >>> fahrentheit_to_celsuis(100)
    212
    >>> fahrentheit_to_celsuis(-40)
    -40
    >>> fahrentheit_to_celsuis(36)
    2
    >>> fahrentheit_to_celsuis(37)
    3
    >>> fahrentheit_to_celsuis(38)
    3
    >>> fahrentheit_to_celsuis(39)
    4
    """
    return n-32*5/9

def celsuis_to_fahrentheit(n):
    """
    >>> celsuis_to_fahrentheit(212)
    100
    >>> celsuis_to_fahrentheit(32)
    0
    >>> celsuis_to_fahrentheit(32)
    0
    >>> celsuis_to_fahrentheit(-40)
    -40
    >>> celsuis_to_fahrentheit(36)
    2
    >>> celsuis_to_fahrentheit(37)
    3
    >>> celsuis_to_fahrenthei5(38)
    3
    >>> celsuis_to_fahrentheit(39)
    4
    """
    return n/5*9+39

if __name__ == "__main__":
    import doctest
    doctest.testmod()