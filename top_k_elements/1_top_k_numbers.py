"""
Given an unsorted array of numbers, find the ‘K’ largest numbers in it.

Example 1:
Input: [3, 1, 5, 12, 2, 11], K = 3
Output: [5, 12, 11]

Example 2:
Input: [5, 12, 11, -1, 12], K = 3
Output: [12, 11, 12]

Time Complexity: O(K * logK + (N-K) * logK) -> O(N * logK)
Space Complexity: O(K)
"""

from heapq import *


def find_k_largest_numbers(nums, k):
    min_heap = []

    # O(K * logK)
    for i in range(k):
        heappush(min_heap, nums[i])

    # O(N-K)
    for i in range(k, len(nums)):

        # O(logK)
        if nums[i] > min_heap[0]:
            heappop(min_heap)
            heappush(min_heap, nums[i])

    return min_heap


def main():
    print("Here are the top K numbers: " +
          str(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3)))

    print("Here are the top K numbers: " +
          str(find_k_largest_numbers([5, 12, 11, -1, 12], 3)))


main()


"""
[3, 1, 5, 12, 2, 11], K = 3

0 - 3
[3]

1 - 1
[1, 3]

2 - 5
[1, 3, 5]

----

3 - 12
12 > 1 -> [3, 5, 12]

4 - 2
2 > 3 -> False

5 - 11
11 > 3 -> [5, 12, 11]
"""