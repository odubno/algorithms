

def is_balanced(s1, s2):
    """
    :param s1:
    :param s2:
    :return:
    Identify whether 2 parentheses are balanced.
    Return True if they are balanced.
    """
    p = {
        '[': ']',
        '(': ')',
        '{': '}',
    }
    return p.get(s1, '') == s2

# slowest but cleanest :D
def balance_check(s):
    """
    :param s:
    :return:
    Given a string of opening and closing parantheses, check whether it's balanced.
    _________
    Taking the recursive approach.
    1. Iterate over the string until a balanced match of two parantheses is made.
    2. Index out the matched parantheses from string "s" and recursively call the function again on "s".
    3. Keep the loop going until all matches are removed.
    4. If the loop completes and any unmatched paranetheses exist, ie length of "s" is greater than 0, return False
    5. If the loop completes and all balanced parantheses have been indexed out, ie len(s) == 0 return True
    """
    if len(s) == 0:
        return True  # 5
    for index in range(len(s)-1):  # 1
        first = s[index]
        second = s[index+1]
        if is_balanced(first, second):  # 1
            s = s[:index] + s[index+2:]  # 2
            return balance_check(s)  # 2
    return False  # 4

# The fastest function
def balance_check2(s):
    chars = []
    matches = {')':'(',']':'[','}':'{'}
    for c in s:
        if c in matches:
            if chars.pop() != matches[c]:
                return False
        else:
            chars.append(c)
    return chars == []

# 2nd place in speed
def balance_check3(s):
    if len(s) % 2 != 0:
        return False
    opening = {'(', '[', '{'}
    matches = {('(', ')'), ('[', ']'), ('{', '}')}
    stack = []
    for paren in s:
        if paren in opening:
            stack.append(paren)
        else:
            if len(stack) == 0:
                return False
            last_open = stack.pop()
            if (last_open, paren) not in matches:
                return False
    return len(stack) == 0

print balance_check('[') == False
print balance_check('[]()') == True
print balance_check3('[](){([[[]]])}') == True
print balance_check('()(){]}') == False

# %timeit balance_check('[](){([[[]]])}')
# %timeit balance_check2('[](){([[[]]])}')
# %timeit balance_check3('[](){([[[]]])}')