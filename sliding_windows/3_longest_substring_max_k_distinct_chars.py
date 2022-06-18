"""
Given a string, find the length of the longest substring in it with no more than K distinct characters.

Example 1:
Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".

Example 2:
Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".

Example 3:
Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".

Example 4:
Input: String="cbbebi", K=10
Output: 6
Explanation: The longest substring with no more than '10' distinct characters is "cbbebi".
"""


def longest_substring_with_k_distinct(str1, k):
    """
    Time Complexity: O(N)
    Space Complexity: O(K) (Where K is the number of characters within the substring)
    :param str1: String
    :param k: Max number of distinct characters
    :return:
    """
    longest_substring = 0
    window_start = 0
    substring = []

    for window_end in range(len(str1)):

        substring += str1[window_end]

        if len(set(substring)) <= k:

            longest_substring = max(longest_substring, len(substring))

        else:

            substring.pop(0)
            window_start += 1

    return longest_substring


def main():
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 2)))
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 1)))
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 3)))


main()
