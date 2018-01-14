

def reverse(s):
    """
    :param s:
    :return:
    Recursively reverse the input string
    """
    # Base Case
    if not s:
        return ''
    # Recursive Case
    return reverse(s[1:]) + s[0]

def reverse2(s):
    """
    :param s:
    :return:
    Recursively reverse the input string
    """
    # Base Case
    if not s:
        return ''

    # Recursive Case
    return s[-1] + reverse(s[:-1])

memo = {}
def reverse3(s):
    """
    :param s:
    :return:
    Recursively reverse the input string
    Uses memoization
    """
    if not s:
        return ''
    if s not in memo:
        memo[s] = reverse2(s[1:]) + s[0]
    return memo[s]



class Memoization:

    def __init__(self, func):
        self.func = func
        self.remember = {}

    def __call__(self, *args):
        if args not in self.remember:
            self.remember[args] = self.func(*args)
        return self.remember[args]


if __name__ == '__main__':
    # r = Memoization(reverse)
    # print r('hello world')
    reverse2('hello world')
    pass