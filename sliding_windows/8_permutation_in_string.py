"""
Given a string and a pattern, find out if the string contains any permutation of the pattern.

Permutation is defined as the re-arranging of the characters of the string. For example, “abc” has the following six permutations:

abc
acb
bac
bca
cab
cba
If a string has ‘n’ distinct characters, it will have n! permutations.

Example 1:
Input: String="oidbcaf", Pattern="abc"
Output: true
Explanation: The string contains "bca" which is a permutation of the given pattern.

Example 2:
Input: String="odicf", Pattern="dc"
Output: false
Explanation: No permutation of the pattern is present in the given string as a substring.

Example 3:
Input: String="bcdxabcdy", Pattern="bcdyabcdx"
Output: true
Explanation: Both the string and the pattern are a permutation of each other.

Example 4:
Input: String="aaacb", Pattern="abc"
Output: true
Explanation: The string contains "acb" which is a permutation of the given pattern.
"""


def find_permutation(string, pattern):

    """
    Time Complexity: O(N + M)
    Space Complexity: O(M)
    :param string:
    :param pattern:
    :return:
    """

    # Fill the pattern_dict
    pattern_dict = {}

    # O(M)
    for char in pattern:
        if char not in pattern_dict:
            pattern_dict[char] = 0
        pattern_dict[char] += 1

    # Sliding Window
    window_start = 0
    matches = 0

    # O(N)
    for window_end in range(len(string)):

        right_car = string[window_end]

        if right_car in pattern_dict:
            pattern_dict[right_car] -= 1

            if pattern_dict[right_car] == 0:
                matches += 1

        if matches == len(pattern_dict):
            return True

        if window_end >= len(pattern) - 1:
            left_char = string[window_start]
            window_start += 1

            if left_char in pattern_dict:

                if pattern_dict[left_char] == 0:
                    matches -= 1

                pattern_dict[left_char] += 1

    return False


def main():
    print('Permutation exist: ' + str(find_permutation("oidbcaf", "abc")))
    print('Permutation exist: ' + str(find_permutation("odicf", "dc")))
    print('Permutation exist: ' + str(find_permutation("bcdxabcdy", "bcdyabcdx")))
    print('Permutation exist: ' + str(find_permutation("aaacb", "abc")))


main()
"""
fbca    abc

{a: 1, b: 1, c: 1}

ws 0 m 0 we 0
f

ws 0 m 0 we 1
b -> {a: 1, b: 0, c: 1} -> m = 1

ws 0 m 1 we 2
c -> {a: 1, b: 0, c: 0} -> m = 2

ws 0 m 2 we 3
a -> {a: 0, b: 0, c: 0} -> m = 3 -> TRUE
"""
