# import sys
#
# n = 10
# data = []
#
# for i in range(50):
#     a = len(data)
#     b = sys.getsizeof(data)
#     # as you increase length, the size and bytes increase from 64 to 96 and so on
#     print 'Length: %s; Size in bytes: %s' % (a, b)
#     data.append(n)

# The key is to provide means to grow the array A that stores elements of a list.


import ctypes
import sys

class DynamicArray():

    def __init__(self):
        """
        set the count of attributes, "n", to 0.
        the capacity of the array begins with being able to hold 1 element.
        actually create the array using make_array()
        """
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    def __len__(self):
        """
        :return:
        the count of the array
        """
        return self.n

    def __getitem__(self, item):
        """
        :param item:
        :return:
        index out an item in array if it exists
        otherwise raise exception
        """
        if not 0 <= item or not item < self.n:
            return IndexError('Item is out of bounds!')
        return self.A[item]

    def append(self, item):
        """
        :param item:
        :return:
        Check capacity
        """
        if self.n == self.capacity:
            self._resize(2 * self.capacity)  # 2x if not enough capacity
        self.A[self.n] = item
        self.n += 1

    def _resize(self, new_capacity):
        B = self.make_array(new_capacity)
        for k in range(self.n):
            B[k] = self.A[k]
        self.A = B
        self.capacity = new_capacity

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

if __name__ == '__main__':
    arr = DynamicArray()
    for i in range(100):
        arr.append(i)
        print sys.getsizeof(arr), sys.getsizeof(i)

    print 'pass'


