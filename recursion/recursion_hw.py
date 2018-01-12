# Problem 1

def rec_sum(n):
    """
    :param n:
    :return:
    A recursive function that takes an integer and computes the cumulative sum of that integer.
    Eg: n=4, return 4+3+2+1+0 which is 10
    """
    if n == 0:
        return 0
    else:
        return n + rec_sum(n - 1)

# Problem 2

def sum_func(n):
    """
    :param n:
    :return:
    Returns the sum of all individual digits in that integer n
    Eg: n=4321, return 4+3+2+1
    """
    if not n:
        return 0
    else:
        return n % 10 + sum_func((n - 1)/10)

def sum_func2(n):
    """
    :param n:
    :return:
    Returns the sum of all individual digits in that integer n
    Eg: n=4321, return 4+3+2+1
    """
    n = str(n)
    if not n:
        return 0
    else:
        return int(n[-1]) + int(sum_func2(n[:-1]))



if __name__ == '__main__':
    # print rec_sum(4)
    print sum_func2(4325)
    pass