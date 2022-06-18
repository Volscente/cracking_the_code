"""
Given a string and a pattern, find all anagrams of the pattern in the given string.

Every anagram is a permutation of a string. As we know, when we are not allowed to
repeat characters while finding permutations of a string, we get N! permutations (or anagrams) of a string having N
characters. For example, here are the six anagrams of the string “abc”:

abc
acb
bac
bca
cab
cba

Write a function to return a list of starting indices of the anagrams of the pattern in the given string.

Example 1:
Input: String="ppqp", Pattern="pq"
Output: [1, 2]
Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".

Example 2:
Input: String="abbcabc", Pattern="abc"
Output: [2, 3, 4]
Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".
"""


def find_string_anagrams(str1, pattern):
    """
    Time Complexity: O(N + M)
    Space Complexity: O(M)
    :param str1:
    :param pattern:
    :return:
    """
    result_indexes = []

    # Create pattern char frequency
    pattern_dict = {}

    for char in pattern:
        if char not in pattern_dict:
            pattern_dict[char] = 0
        pattern_dict[char] += 1

    # Sliding Window
    window_start, matches = 0, 0

    for window_end in range(len(str1)):

        right_char = str1[window_end]

        if right_char in pattern_dict:
            pattern_dict[right_char] -= 1

            if pattern_dict[right_char] == 0:
                matches += 1

        if matches == len(pattern_dict):
            result_indexes.append(window_start)

        if window_end >= len(pattern) - 1:
            left_char = str1[window_start]
            window_start += 1

            if left_char in pattern_dict:
                if pattern_dict[left_char] == 0:
                    matches -= 1
                pattern_dict[left_char] += 1

    return result_indexes


def main():
    print(find_string_anagrams("ppqp", "pq"))
    print(find_string_anagrams("abbcabc", "abc"))


main()
