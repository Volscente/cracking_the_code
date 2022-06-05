"""
Design a class to calculate the median of a number stream. The class should have the following two methods:

1. insertNum(int num): stores the number in the class
2. findMedian(): returns the median of all numbers inserted in the class

If the count of numbers inserted in the class is even, the median will be the average of the middle two numbers.

Time Complexity: insert_sum is O(logN) and find_median is O(1)
Space Complexity: O(N)
"""

from heapq import *


class MedianOfAStream:
    max_heap, min_heap = [], []

    def insert_num(self, num):

        # Insertion phase
        if not self.max_heap or -self.max_heap[0] >= num:
            heappush(self.max_heap, -num)
        else:
            heappush(self.min_heap, num)

        # Balance phase
        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.max_heap) < len(self.min_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

    def print_heaps(self):

        print('Max Heap')
        print(self.max_heap)
        print('\n')
        print('Min Heap')
        print(self.min_heap)

    def find_median(self):

        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0

        return -self.max_heap[0] / 1.0


def main():

    median_stream = MedianOfAStream()
    median_stream.insert_num(3)
    median_stream.insert_num(1)
    print("The median is: " + str(median_stream.find_median()))
    median_stream.insert_num(5)
    print("The median is: " + str(median_stream.find_median()))
    median_stream.insert_num(4)
    print("The median is: " + str(median_stream.find_median()))


main()
