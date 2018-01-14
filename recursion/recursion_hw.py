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

# Problem 3

# The fasters of the 3
def word_split(phrase, list_of_words, output=None, word=''):
    """
    :param phrase:
    :param list_of_words:
    :param output:
    :return:
    Split a continuous phrase with no spaces into a individual words.
    Use a the list of provided words to match against.
    Eg. function word_split('ilovedogsJohn', ['i', 'am', 'a', 'dogs', 'lover', 'love', 'John'])
    should return ['i', 'love', 'dogs', 'John']
    """
    if not output:
        output = []
    if not phrase:
        return output
    word += phrase[0]
    if word in list_of_words:
        output.append(word)
        word = ''
    return word_split(phrase[1:], list_of_words, output=output, word=word)

def word_split2(phrase, list_of_words, output=None):
    """
    :param phrase:
    :param list_of_words:
    :param output:
    :return:
    Split a continuous phrase with no spaces into a individual words.
    Use a the list of provided words to match against.
    Eg. function word_split('ilovedogsJohn', ['i', 'am', 'a', 'dogs', 'lover', 'love', 'John'])
    should return ['i', 'love', 'dogs', 'John']
    """
    if not output:
        output = []
    for word in list_of_words:
        if phrase.startswith(word):
            output.append(word)
            word_split2(phrase[len(word):], list_of_words, output)
    return output

# The slowest of the 3
def word_split3(phrase, list_of_words, output=None, count=0):
    """
    :param phrase:
    :param list_of_words:
    :param output:
    :return:
    Split a continuous phrase with no spaces into a individual words.
    Use a the list of provided words to match against.
    Eg. function word_split('ilovedogsJohn', ['i', 'am', 'a', 'dogs', 'lover', 'love', 'John'])
    should return ['i', 'love', 'dogs', 'John']
    """
    count += 1
    if not output:
        output = []
    if not phrase or count == len(phrase):
        return output
    word = list_of_words[0]
    if phrase.startswith(word):
        output.append(word)
        phrase = phrase[len(word):]
    list_of_words = list_of_words[1:]
    list_of_words.append(word)  # move word to the end of the list
    return word_split3(phrase, list_of_words, output, count=count)


if __name__ == '__main__':
    # print rec_sum(4)
    print sum_func2(4325)

    print word_split3('themanran',['clown','ran','man'])
    print word_split('lovedogsJohn', ['am', 'a', 'dogs', 'lover', 'love', 'John'])
    print word_split3('themanran', ['the', 'ran', 'man'])
    pass