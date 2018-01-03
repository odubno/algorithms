import timeit

def func_constant(lst):
    """
    O(1) Constant
    """
    print lst[0]

def func_linear(lst):
    """
    O(n) Linear
    """
    for val in lst:
        print val

def func_quadratic(lst):
    """
    O(n^2) Quadratic
    """
    for item_1 in lst:
        for item_2 in lst:
            print item_1, item_2

def print_once(lst):
    """
        O(2)
    """
    for val in lst:
        print val

def print_2(lst):
    """
    O(2n)
    """
    for val in lst:
        print val
    for val in lst:
        print val

def comp(lst):
    """
    Order of the function
    complete: O(1 + n/2 + 10)
    simplified: O(n)
    """

    print lst[0]  #O(1)

    midpoint = len(lst)/2
    for val in lst[:midpoint]:
        # O(n/2)
        print val

    for x in range(10):
        # O(10)
        print 'hello world.'

def matcher(lst, match):
    """
    lst = [1, 2, 3]
    matcher(lst, 1): True : O(1) best case
    matcher(lst, 4): False : O(n) worst case
    """
    for item in lst:
        if item == match:
            return True
    return False

def create_list(n):
    """
    create_list(3): ['new', 'new', 'new']
    Space Complexity of O(n). This will take up "n" items in memory.
    """
    new_list = []
    for num in range(n):
        new_list.append('new')
    return new_list

def printer(n):
    """
    Time Complexity: O(n)
    Space Complexity: O(1) eg. the same thing is getting printed each time.
    """
    for x in range(10):
        print 'hello world!'

lst = [1, 2, 3]
# func_constant(lst)
# func_linear(lst)
# func_quadratic(lst)
# print_once(lst)
comp(lst)