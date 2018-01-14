
factorial_memo = {}

def factorial(k):
    """
    :param k:
    :return:
    %timeit factorial(100)
    1000000 loops, best of 3: 234 ns per loop
    """
    # using memoization is way faster than using regular recursion
    if k < 2:
        return 1
    if k not in factorial_memo:
        factorial_memo[k] = k * factorial(k-1)
    return factorial_memo[k]

def factorial2(k):
    """
    :param k:
    :return:
    # %timeit factorial2(100)
    10000 loops, best of 3: 25.2 us per loop
    """
    if k < 2:
        return 1
    return k * factorial2(k-1)

class Memoize:
    """
    Implements your own call function
    """
    def __init__(self, f):
        self.f = f
        self.memo = {}

    def call(self, k):
        if k not in self.memo:
            self.memo[k] = self.f(k)
        return self.memo[k]

class Memoize2:
    """
    - This method of recursion keeps, 'remembers', the cache of results from the function.
    - The function returns the remembered result.
    """
    def __init__(self, f):
        self.f = f
        self.memo = {}

    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]

if __name__ == '__main__':
    # print factorial(4)
    # print factorial2(4)
    factorial = Memoize(factorial2)
    factorial2 = Memoize2(factorial2)
    factorial.call(4)
    factorial2(4)
    print 'pass'