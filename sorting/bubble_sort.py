# The goal is to move larger numbers up and index smaller numbers to the bottom.
# Time Complexity: O(n^2)


def bubbleSort(my_list):
    l = len(my_list)
    for n1 in range(l):
        for n2 in range(l-1):
            if my_list[n2] > my_list[n1]:
                my_list[n2], my_list[n1] = my_list[n1], my_list[n2]

def bubbleSort2(my_list):
    l = len(my_list)-1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(l):
            if my_list[i] > my_list[i+1]:
                my_list[i+1], my_list[i] = my_list[i], my_list[i+1]
                sorted = False
    return my_list


if __name__ == '__main__':
    l = [5,3,8,1, 10, 100, 7, 4, 5, 11]
    bubbleSort2(l)
    print(l)