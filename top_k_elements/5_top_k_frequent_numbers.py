"""
Given an unsorted array of numbers, find the top ‘K’ frequently occurring numbers in it.

Example 1:
Input: [1, 3, 5, 12, 11, 12, 11], K = 2
Output: [12, 11]
Explanation: Both '11' and '12' appeared twice.

Example 2:
Input: [5, 12, 11, 3, 11], K = 2
Output: [11, 5] or [11, 12] or [11, 3]
Explanation: Only '11' appeared twice, all other numbers appeared once.
"""

from heapq import *


def find_k_frequent_numbers(nums, k):
    """
    Time Complexity: O(N + N*logN)
    Space Complexity: O(N)
    :param nums:
    :param k:
    :return:
    """
    top_frequent_numbers = []
    freq_dict = {}
    min_heap = []

    # O(N)
    for num in nums:
        if num not in freq_dict:
            freq_dict[num] = 0
        freq_dict[num] += 1

    # O(N * logN)
    for num, freq in freq_dict.items():
        heappush(min_heap, (freq, num))

    # O((N-K) * logN)
    while len(min_heap) > k:
        heappop(min_heap)

    # O(N)
    for node in min_heap:
        top_frequent_numbers.append(node[1])

    return top_frequent_numbers


def main():
    print("Here are the K frequent numbers: " +
          str(find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2)))

    print("Here are the K frequent numbers: " +
          str(find_k_frequent_numbers([5, 12, 11, 3, 11], 2)))


main()

"""
[1, 3, 5, 12, 11, 12, 11]

{1: 1, 3:1, 5:1, 12:2, 11:2}

[(1, 1), (1, 3), (1, 5), (2, 12), (2, 11)]
"""
