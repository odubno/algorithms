
def factorial(n):
    if n == 0:
        # Base Case
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == '__main__':
    print factorial(4)