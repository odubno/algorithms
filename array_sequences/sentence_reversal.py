

def rev_word(s):
    """
    :param s:
    :return:
    1. append an empty space at the end of the string to add an extra loop in case the iteration finishes to early.
    2. Iterate over the string
    3. If character is not an empty space add letters together
    4. During every new space append the current string of letters to the beginning of rev_words list
    5. Return the reversed string of words
    """
    rev_words = []
    word = ''
    s = s + ' '  # 1
    for i in s:  # 2
        if i != ' ':  # 3
            word += i
            continue
        if word:
            rev_words = [word] + rev_words  # 4
        word = ''
    return ' '.join(rev_words)  # 5

def rev_word2(s):
    arr = s.split()
    rev = arr[::-1]
    return ' '.join(rev)


def rev_word3(s):
    """
    Manually doing the splits on the spaces.
    """

    words = []
    length = len(s)
    spaces = [' ']

    # Index Tracker
    i = 0

    # While index is less than length of string
    while i < length:

        # If element isn't a space
        if s[i] not in spaces:

            # The word starts at this index
            word_start = i

            while i < length and s[i] not in spaces:
                # Get index where word ends
                i += 1
            # Append that word to the list
            words.append(s[word_start:i])
        # Add to index
        i += 1

    # Join the reversed words
    return " ".join(reversed(words))

def rev_words4(s):
    """
    :param s:
    :return:
    Recursively reverse the input string
    """
    # Base Case
    if not s:
        return ''
    # Recursive Case
    return reverse(s[1:]) + ' ' + s[0]

rev_word2('Hi John,   are you ready to go?')

print rev_word('Hi John,   are you ready to go?') == 'go? to ready you are John, Hi'
print rev_word('    space before') == 'before space'
print rev_word('space after     ') == 'after space'
print rev_word('   Hello John    how are you   ') == 'you are how John Hello'
print rev_word('1') == '1'

# %timeit rev_word('Hi John,   are you ready to go?')
# %timeit rev_word2('Hi John,   are you ready to go?')
# %timeit rev_word3('Hi John,   are you ready to go?')