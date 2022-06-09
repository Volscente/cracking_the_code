"""
Given an array of numbers and a number ‘k’, find the median of all the ‘k’ sized sub-arrays (or windows) of the array.

Example 1:

Input: nums=[1, 2, -1, 3, 5], k = 2
Output: [1.5, 0.5, 1.0, 4.0]
Explanation: Lets consider all windows of size ‘2’:

[ 1, 2, -1, 3, 5] -> median is 1.5
[1, 2, -1, 3, 5] -> median is 0.5
[1, 2, -1, 3, 5] -> median is 1.0
[1, 2, -1, 3, 5] -> median is 4.0

Time Complexity: O(N * K) where N is the len(nums) and k is the size of the window. Inserting/removing from heaps is O(logK)
Space Complexity: O(K)
"""


import heapq


class SlidingWindowMedian:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def insert_node(self, num):

        if not self.max_heap or -self.max_heap[0] >= num:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

    def rebalance_heaps(self):

        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.max_heap) < len(self.min_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def compute_median(self):

        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        return -self.max_heap[0] / 1.0

    def remove_node(self, heap, num):

        index = heap.index(num)
        heap[index] = heap[-1]
        del heap[-1]

        if index < len(heap):
            heapq._siftup(heap, index)
            heapq._siftdown(heap, 0, index)

    def find_sliding_window_median(self, nums, k):

        result = [0.0 for x in range(len(nums) - k + 1)]

        for i in range(0, len(nums)):

            self.insert_node(nums[i])
            self.rebalance_heaps()

            if i - k + 1 >= 0:

                result[i - k + 1] = self.compute_median()

                if nums[i - k + 1] <= -self.max_heap[0]:
                    self.remove_node(self.max_heap, -nums[i - k + 1])
                else:
                    self.remove_node(self.min_heap, nums[i - k + 1])

                self.rebalance_heaps()

        return result


def main():
    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median(
        [1, 2, -1, 3, 5], 2)
    print("Sliding window medians are: " + str(result))

    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median(
        [1, 2, -1, 3, 5], 3)
    print("Sliding window medians are: " + str(result))


main()
