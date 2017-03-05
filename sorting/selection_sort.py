# Selection Sort takes the index of the first number and makes sure it's the smallest
# by checking it against all of the numbers in the list.
# If there's a smaller number in the list, then the selection sort
# will swap the indexes of those numbers.



def selectionSortSmall(my_list):
    """
    :return: Selects the index of the first number and searches for smallest number
    """
    length = len(my_list)
    for i in range(length):
        smallest_index = i
        for i2 in range(i+1, length):
            if my_list[smallest_index] > my_list[i2]:
                smallest_index = i2
        my_list[i], my_list[smallest_index] = my_list[smallest_index], my_list[i]
    return my_list


def selectionSortLarge(my_list):
    """
    :return: Selects the index of the last number and searches for the largest number
    """
    length = len(my_list)
    reversed = range(length - 1, -1, -1)
    for i in reversed:
        large = i
        reversed2 = range(large - 1, -1, -1)
        for i2 in reversed2:
            if my_list[i2] > my_list[large]:
                large = i2
        my_list[i], my_list[large] = my_list[large], my_list[i]
    return my_list



if __name__ == '__main__':
    l = [7, 5, 3, 6, 4, 8, 9, 1]
    print(selectionSortLarge(l))
    print(l)