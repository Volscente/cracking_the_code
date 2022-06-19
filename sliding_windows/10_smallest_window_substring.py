"""
Given a string and a pattern, find the smallest substring in the given string which has all the character occurrences of the given pattern.

Example 1:
Input: String="aabdec", Pattern="abc"
Output: "abdec"
Explanation: The smallest substring having all characters of the pattern is "abdec"

Example 2:
Input: String="aabdec", Pattern="abac"
Output: "aabdec"
Explanation: The smallest substring having all character occurrences of the pattern is "aabdec"

Example 3:
Input: String="abdbca", Pattern="abc"
Output: "bca"
Explanation: The smallest substring having all characters of the pattern is "bca".

Example 4:
Input: String="adcad", Pattern="abc"
Output: ""
Explanation: No substring in the given string has all characters of the pattern.
"""


def find_substring(string, pattern):
    """
    Time Complexity: O(N + M)
    Space Complexity: O(N) [Worst case we need N characters to store the whole string as substring]
    :param string:
    :param pattern:
    :return:
    """
    min_substring = ""
    window_start = 0
    matched_char = 0

    # Construct dictionary of pattern
    pattern_freq_dict = {}

    # O(M)
    for char in pattern:
        if char not in pattern_freq_dict:
            pattern_freq_dict[char] = 0
        pattern_freq_dict[char] += 1

    # Sliding Window over the String
    # O(N)
    for window_end in range(len(string)):

        right_char = string[window_end]

        if right_char in pattern_freq_dict:
            pattern_freq_dict[right_char] -= 1

            if pattern_freq_dict[right_char] == 0:
                matched_char += 1

        while matched_char == len(pattern_freq_dict):

            if len(min_substring) == 0 or len(min_substring) > window_end - window_start + 1:
                min_substring = string[window_start:window_end + 1]

            left_char = string[window_start]
            window_start += 1

            if left_char in pattern_freq_dict:
                if pattern_freq_dict[left_char] == 0:
                    matched_char -= 1
                pattern_freq_dict[left_char] += 1

    return min_substring


def main():
    print(find_substring("aabdec", "abc"))
    print(find_substring("aabdec", "abac"))
    print(find_substring("abdbca", "abc"))
    print(find_substring("adcad", "abc"))


main()


"""
string = abac pattern = bc -> bac

ms "" ws 0 mc 0
{b: 1, c: 1}

we 0 a

we 1 b
{b: 0, c: 1} -> mc 1

we 2 a

we 3 c
{b: 0, c: 0} -> mc 2 -> ms "abac" -> a ws 1 -> mc == 2 -> len(ms) = 4 len(window) = 3 -> ms = 'bac' -> b
mc = 1 {b: 1, c:0}

return 'bac'
"""
