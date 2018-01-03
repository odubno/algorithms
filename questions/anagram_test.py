from nose.tools import assert_equal
from anagram_check import anagram

class AnagramTest(object):

    def test(self, sol):
        assert_equal(sol('go go go', 'gggooo'), True)
        assert_equal(sol('abc', 'cba'), True)
        assert_equal(sol('hi man', 'hi     man'), True)
        assert_equal(sol('aabbcc', 'aabbc'), False)
        assert_equal(sol('123', '1 2'), False)
        print('ALL TEST CASES PASSED')


if __name__ == '__main__':
    t = AnagramTest()
    t.test(anagram)