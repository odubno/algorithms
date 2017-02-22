# Goal: find item in the list
# traversing the list until the element is found
# Time complexity is: O(n) Linear Time Complexity

def forwardIteration(myItem, myList):
    """
    :return: Forward Iteration
    Using a while loop to iterate over the list while increasing the index until the index
    exceeds the length of the list.
    """
    index = 0
    length = len(myList)
    while index < length:
        if myList[index] == myItem:
            return True
        index += 1
    return False


def forwardIteration2(myItem, myList):
    """
    :return: Forward Iteration
    Using a for loop, iterate over each item until the one we want is found else return None
    """
    for item in myList:
        if item == myItem:
            return True
    return False


def forwardIteration3(myItem, myList):
    """
    :return: Forward Iteration
    The list is traversed from beginning to end, using range of the list to index out items
    until the item is found.
    """
    start = 0
    length = len(myList)
    for index in range(start, length):
        if myList[index] == myItem:
            return True
    return False



def recursive(myItem, myList):
    """
    :return: Recursive Version
    If the value is found at the first index we return True
    else we index out the 0 index item and call the function again.
    We continue to call the function and index out items from the beginning
    until the end of the list.
    """
    if len(myList) != 0:
        if myList[0] == myItem:
            return True
        else:
            myList = myList[1:]
            return recursive(myItem, myList)
    return False



def reverseSearch(myItem, myList):
    """
    :return: Reverse Search
    A variation on the Forward Search.
    Starting from the last index if the element is found we return True
    """
    index = len(myList) - 1
    while index >= 0:
        if myList[index] == myItem:
            return True
        index -= 1
    return False


def sentinelSearch(myItem, myList):
    """
    :return: sentinelSearch
    appending myItem to the end of the list to guarantee exit from while loop
    This method reduces the overhead cost of calling the len(myList) and instead indexes out items
    one by one until the item is found and returns the index.
    The optimization isn't much though.
    """
    myList.append(myItem)
    index = 0
    while True:
        if myList[index] == myItem:
            break
        index += 1
    return index


def ordredListSearch(myItem, myList):
    """
    :return: Ordered List Search
    This would only apply to list of items whose items are ordered according to length
    """
    index = 0
    while True:
        assert index < len(myList)
        if myList[index] == myItem:
            return True
        elif myList[index] > myItem:
            return False
        else:
            index += 1


if __name__=='__main__':
    shopping = ['apples','bananas','chocolate','pasta']
    item = 'candy'

    f = forwardIteration(item, shopping)
    if f:
        print('%s is in the list' % item)
    else:
        print('Item not in list.')