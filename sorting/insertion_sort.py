# Insertion sort loops over the range (length of the list) and checks each index value against the preceding index value

def insertionSort(my_list):
    l = len(my_list)
    for i in range(1, l):
        current_value = my_list[i]
        position = i
        while position > 0 and my_list[position-1] > current_value:
            my_list[position] = my_list[position-1]
            position -= 1
        my_list[position] = current_value



if __name__ == '__main__':
    l = [7,5,3,6,4,8,9,1]
    insertionSort(l)
    print(l)

