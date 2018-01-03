import re
from collections import defaultdict
from collections import Counter

def anagram(s1, s2):
    """
    :param s1: string
    :param s2: string
    :return:
    Checking if two strings match
    """
    s1 = re.findall('\w', s1.lower())
    s2 = re.findall('\w', s2.lower())
    s3 = []
    if len(s1) != len(s2):
        return False
    for i1 in s1:
        for i2 in s2:
            if i1 == i2:
                s2.remove(i2)
                s3.append(i2)
                break
    if s1 != s3:
        return False
    return True


def anagram2(s1, s2):
    # grab only letters and make sure they're all lowercase
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
    if len(s1) != len(s2):
        # if the length of both strings do not match than they're not an anagram
        return False
    count = defaultdict(int)
    for letter in s1:
        count[letter] += 1
    for letter in s2:
        count[letter] -= 1
    if any(count.values()):
        # Check that all counts are 0
        return False
    # Otherwise they're anagrams
    return True

def anagram3(s1, s2):
    # grab only letters and make sure they're all lowercase
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
    if len(s1) != len(s2):
        # if the length of both strings do not match than they're not an anagram
        return False
    count1 = Counter(s1)
    count2 = Counter(s2)
    if count1 != count2:
        return False
    return True

def anagram4(s1, s2):
    # Remove spaces and lowercase letters
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    # Edge Case to check if same number of letters
    if len(s1) != len(s2):
        return False

    # Create counting dictionary (Note could use DefaultDict from Collections module)
    count = {}

    # Fill dictionary for first string (add counts)
    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    # Fill dictionary for second string (subtract counts)
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    # Check that all counts are 0
    for k in count:
        if count[k] != 0:
            return False

    # Otherwise they're anagrams
    return True

anagram3('public relations is great', 'Crap Built on lies is great')
# %timeit anagram('public relations is great', 'Crap Built on lies is great')
# %timeit anagram2('public relations is great', 'Crap Built on lies is great')
# %timeit anagram3('public relations is great', 'Crap Built on lies is great')
# %timeit anagram4('public relations is great', 'Crap Built on lies is great')
pass