from nose.tools import assert_equal
from balance_check import balance_check


class TestBalanceCheck(object):
    def test(self, sol):
        assert_equal(sol('[](){([[[]]])}('), False)
        assert_equal(sol('[{{{(())}}}]((()))'), True)
        assert_equal(sol('[[[]])]'), False)
        print ('ALL TEST CASES PASSED')


# Run Tests

t = TestBalanceCheck()
t.test(balance_check)