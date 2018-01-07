
def uniq_char(s):
    count = set()
    for i in s:
        if i in count:
            return False
        else:
            count.add(i)
    return True

def uniq_char2(s):
    return len(set(s)) == len(s)

uniq_char('abcde')
uniq_char('aabcde')

print uniq_char('') == True
print uniq_char('goo') == False
print uniq_char('abcdefg') == True

# %timeit uniq_char('abcde')
# %timeit uniq_char2('abcde')