from collections import OrderedDict

def compress(s):
    count = OrderedDict()
    for i in s:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    result = [k + str(v) for k, v in count.iteritems()]
    return ''.join(result)

def compress2(s):
    """
    :param s: string of letters
    :return:
    Compress a string by counting each character, eg
    input: 'AAAAABBBBCCCC'
    result: 'A5B4C4'
    ______________________
    1. Create an edge case
    2. Index out the first character of the string and set the count equal to 1
    3. The result will be a string. We start with an empty string
    4. Loop over the characters in the string. Keep counting the character until it's different from the last
    5. Append the string results of letter, count combination to the "result" string
    6. Reset the count and start a new count of the next letter.
    """
    if not s:  # 1
        return ''
    start_letter = s[0]
    count = 1  # 2
    result = ''  # 3
    for next_letter in s[1:]:  # 4
        if start_letter == next_letter:  # 4
            count += 1
        else:
            # reset everything
            result += '%s%s' % (start_letter, count)  # 5
            count = 1  # 6
            start_letter = next_letter  # 6
    result += '%s%s' % (start_letter, count)
    return result


def compress3(s):
    """
    This solution compresses without checking. Known as the RunLength Compression algorithm.
    """
    # Begin Run as empty string
    r = ""
    l = len(s)
    # Check for length 0
    if l == 0:
        return ""
    # Check for length 1
    if l == 1:
        return s + "1"
    # Intialize Values
    cnt = 1
    i = 1
    while i < l:
        # Check to see if it is the same letter
        if s[i] == s[i - 1]:
            # Add a count if same as previous
            cnt += 1
        else:
            # Otherwise store the previous data
            r = r + s[i - 1] + str(cnt)
            cnt = 1
        # Add to index count to terminate while loop
        i += 1
    # Put everything back into run
    r = r + s[i - 1] + str(cnt)
    return r

compress3('AAAAADDBBBBCCCC')
print compress2('') == ''
print compress2('AABBCC') == 'A2B2C2'
print compress2('AAABCCDDDDD') == 'A3B1C2D5'

# %timeit compress('AAAAADDBBBBCCCC')
# %timeit compress2('AAAAADDBBBBCCCC')
# %timeit compress3('AAAAADDBBBBCCCC')