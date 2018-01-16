
def permute(s):
    """
    Write a function that uses recursion to output a list of all the possible permutations of that string
    :param s:
    :return:
    s='abc' the function should return ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    1. Iterate through the initial string - e.g., 'abc'

    2. For each character in the initial string, set aside that character and get a list of all permutations of
    the string that's left. So, for example, if the currect iteration is on 'b', we'd want t ofind all the
    permutations of the string 'ac'.

    3. Once you have the list from step 2, add each element from that list to the character from the initial string, and
    append the result to out list of final results. So if we're on 'b' and we've gotten the list ['ac', 'ca'], we'd add
    'b' to those, results in 'bac' and 'bca', each of which we'd add to our final results.

    4. Return the list of final results.
    """
    # Base Case
    out = []
    if len(s) == 1:
        out = [s]
    for i, letter in enumerate(s):
        print letter
        # for every letter in the string
        temp = s[:i] + s[i+1:]
        for perm in permute(temp):
            # print perm
            # For every permutation
            out += [letter + perm]
    return out


if __name__ == '__main__':
    permute('abcd')

