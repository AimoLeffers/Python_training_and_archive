import math


def multiply_with_loop_imperfect(x, y):
    return sum(y for _ in range(x))


def multiply_with_loop_better(x, y):
    if (x >= 0 and y >= 0) or (x < 0 and y < 0):
        return sum(abs(y) for _ in range(abs(x)))
    elif x < 0:
        return sum(x for _ in range(y))
    else:
        return sum(y for _ in range(x))


def length_of_integer(n):
    """
    This function calculates the number of digits form a given integer.

    :param n: this is the integer, which number of digits will be calculated
    :return: the number of digits of n
    """
    if type(n) is not int:
        raise TypeError("Invalid Type")

    add = 1 if n >= 0 else 2
    return int(math.floor(math.log10(abs(n))) + add) if n != 0 else 1
