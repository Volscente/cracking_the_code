"""
Given an unsorted array of numbers, find Kth smallest number in it.

Please note that it is the Kth smallest number in the sorted order, not the Kth distinct element.

Example 1:
Input: [1, 5, 12, 2, 11, 5], K = 3
Output: 5
Explanation: The 3rd smallest number is '5', as the first two smaller numbers are [1, 2].

Example 2:
Input: [1, 5, 12, 2, 11, 5], K = 4
Output: 5
Explanation: The 4th smallest number is '5', as the first three small numbers are [1, 2, 5].

Example 3:
Input: [5, 12, 11, -1, 12], K = 3
Output: 11
Explanation: The 3rd smallest number is '11', as the first two small numbers are [5, -1].

Solution:
Apply a Max-Heap of k-dimension. The root will contain the k-smallest number.

Time Complexity: O(K * logK + (N - K) * logK) -> O(N * logK)
Space Complexity: O(K)
"""

from heapq import *


def find_k_th_smallest_number(nums, k):
    max_heap = []

    # O(K * logK)
    for i in range(k):
        heappush(max_heap, -nums[i])

    # O(N-K)
    for i in range(k, len(nums)):

        # O(logK)
        if -nums[i] > max_heap[0]:
            heappop(max_heap)
            heappush(max_heap, -nums[i])

    return -max_heap[0]


def main():
    print("Kth smallest number is: " +
          str(find_k_th_smallest_number([1, 5, 12, 2, 11, 5], 3)))

    # since there are two 5s in the input array, our 3rd and 4th smallest numbers should be a '5'
    print("Kth smallest number is: " +
          str(find_k_th_smallest_number([1, 5, 12, 2, 11, 5], 4)))

    print("Kth smallest number is: " +
          str(find_k_th_smallest_number([5, 12, 11, -1, 12], 3)))


main()
