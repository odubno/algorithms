def finder(arr1, arr2):
    """
    :param arr1: list of numbers
    :param arr2: same list as arr1 but with one missing number
    :return:
    return the missing number that's in arr1 but not in arr2
    1. Iterate over arr1
    2. Check if number is in arr2 and remove it if it is
    3. Otherwise return the number that is not in arr2
    """
    for i in arr1:
        if i in arr2:  # 1
            arr2.remove(i)  # 2
        else:
            return i  # 3
    return None

def finder2(arr1, arr2):
    """
    :param arr1: list of numbers
    :param arr2: same list as arr1 but with one missing number
    :return:
    return the missing number that's in arr1 but not in arr2
    1. Simply find the difference between both sums
    """
    return sum(arr1) - sum(arr2)


def finder3(arr1, arr2):
    result = 0
    # Perform an XOR between the numbers in the arrays
    for num in arr1 + arr2:
        result ^= num
    return result

print finder2([5,5,7,7],[5,7,7]) == 5
print finder2([1,2,3,4,5,6,7],[3,7,2,1,4,6]) == 5
print finder2([1,2,3,4,5,6,7],[3,7,2,1,4,6]) == 5
print finder2([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1]) == 6

# %timeit finder([9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 8, 7, 5, 4, 3, 2, 1])
# %timeit finder2([9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 8, 7, 5, 4, 3, 2, 1])
# %timeit finder3([9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 8, 7, 5, 4, 3, 2, 1])