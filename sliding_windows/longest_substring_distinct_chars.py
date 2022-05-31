"""
Given a string, find the length of the longest substring, which has all distinct characters.

Example 1:
Input: String="aabccbb"
Output: 3
Explanation: The longest substring with distinct characters is "abc".

Example 2:
Input: String="abbbb"
Output: 2
Explanation: The longest substring with distinct characters is "ab".

Example 3:
Input: String="abccde"
Output: 3
Explanation: Longest substrings with distinct characters are "abc" & "cde".
"""


def non_repeat_substring(string):
    max_length = 0
    char_dict = {}

    window_start = 0

    for window_end in range(len(string)):

        if string[window_end] not in char_dict.keys():

            char_dict[string[window_end]] = 1

        else:

            char_dict[string[window_end]] += 1

        while char_dict[string[window_end]] > 1:

            char_dict[string[window_start]] -= 1

            if char_dict[string[window_start]] == 0:
                del char_dict[string[window_start]]

            window_start += 1