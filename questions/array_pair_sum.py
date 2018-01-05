import cProfile

def pair_sum(arr, k, result=0):
    """
    :param arr: a list of integers
    :param k: integer
    :param result: counting unique pairs from arr that sum up to k
    :return:
    ----------
    Given an integer array, output the number of unique pairs that sum up to a specific value k.
    ----------
    1. Create a temporary copy of arr removing the number that we're summing
    2. Iterate over the temp list until a match is found
    3. If a match is found remove the matched integers from arr
    4. Recursively, call pair_sum() again with the new arr
    5. Keep track of all unique pairs
    """
    for first in arr:
        temp = arr[:]  # 1
        temp.remove(first)
        for second in temp:  # 2
            num = first + second
            if num == k:
                arr.remove(first)  # 3
                arr.remove(second)  # 3
                result = pair_sum(arr, k, result)  # 4
                return result + 1  # 5
    return result

def pair_sum2(arr, k):
    if len(arr) < 2:
        return
    # Sets for tracking
    seen = set()
    output = 0
    # For every number in array
    for num in arr:
        # Set target difference
        target = k - num
        # Add it to set if target hasn't been seen
        if target not in seen:
            seen.add(num)
        else:
            # Add a tuple with the corresponding pair
            output += 1
    return output

# print pair_sum2([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1], 10) == 6
# print pair_sum2([1,2,3,1], 3) == 1
# print pair_sum2([1,2,3,2], 4) == 2
# print pair_sum2([1,3,2,2],4) == 2


