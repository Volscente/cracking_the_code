"""
Given a string, sort it based on the decreasing frequency of its characters.

Example 1:
Input: "Programming"
Output: "rrggmmPiano"
Explanation: 'r', 'g', and 'm' appeared twice, so they need to appear before any other character.

Example 2:
Input: "abcbab"
Output: "bbbaac"
Explanation: 'b' appeared three times, 'a' appeared twice, and 'c' appeared only once.
"""

from heapq import *


def sort_character_by_frequency(string):
    """
    Time Complexity O(N + N*logK + K*logK) -> O(N * logK) -> O(N * logN)
    Space Complexity: O(N)
    :param string:
    :return:
    """
    freq_dict = {}
    max_heap = []
    result_string = ''

    # O(N)
    for char in string:
        if char not in freq_dict:
            freq_dict[char] = 0
        freq_dict[char] += 1

    # O(N*logK)
    for char, freq in freq_dict.items():
        heappush(max_heap, (-freq, char))

    # O(K * logK)
    while max_heap:

        freq, char = -max_heap[0][0], max_heap[0][1]

        for i in range(freq):
            result_string += char

        heappop(max_heap)

    return result_string


def main():
    print("String after sorting characters by frequency: " +
          sort_character_by_frequency("Programming"))
    print("String after sorting characters by frequency: " +
          sort_character_by_frequency("abcbab"))


main()

