"""
Given ‘M’ sorted arrays, find the K’th smallest number among all the arrays.

Example 1:
Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4], K=5
Output: 4
Explanation: The 5th smallest number among all the arrays is 4, this can be verified from
the merged list of all the arrays: [1, 2, 3, 3, 4, 6, 6, 7, 8]

Example 2:
Input: L1=[5, 8, 9], L2=[1, 7], K=3
Output: 7
Explanation: The 3rd smallest number among all the arrays is 7.
"""

from heapq import *


def find_kth_smallest(lists, k):
    """
    Time Complexity: O(K * logM)
    Space Complexity: O(M)
    :param lists:
    :param k:
    :return:
    """
    min_heap = []

    # O(M * logM)
    for list_elem in lists:
        heappush(min_heap, (list_elem[0], 0, list_elem))

    count = 0

    # O(K * (logM + logM)
    while min_heap:

        num, index, list_elem = heappop(min_heap)
        count += 1

        if count == k:
            break

        if len(list_elem) > index + 1:
            heappush(min_heap, (list_elem[index + 1], index + 1, list_elem))

    return num


def main():
    print("Kth smallest number is: " +
          str(find_kth_smallest([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5)))


main()
