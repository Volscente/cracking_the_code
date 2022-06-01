def length_of_longest_substring(string, k):

    """
    Given a string with lowercase letters only, if you are allowed to replace no more than k letters with any letter,
    find the length of the longest substring having the same letters after replacement.

    Example 1:
    Input: String="aabccbb", k=2
    Output: 5
    Explanation: Replace the two 'c' with 'b' to have the longest repeating substring "bbbbb".

    Example 2:
    Input: String="abbcb", k=1
    Output: 4
    Explanation: Replace the 'c' with 'b' to have the longest repeating substring "bbbb".

    Example 3:
    Input: String="abccde", k=1
    Output: 3
    Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".

    Time Complexity: O(N)
    Space Complexity: O(1)
    :param string:
    :param k:
    :return:
    """

    chars_dict = {}
    max_length = 0
    max_repeat_letter = 0
    window_start = 0

    for window_end in range(len(string)):

        if string[window_end] not in chars_dict:
            chars_dict[string[window_end]] = 0

        chars_dict[string[window_end]] += 1

        max_repeat_letter = max(max_repeat_letter, chars_dict[string[window_end]])

        if (window_end - window_start + 1 - max_repeat_letter) > k:

            chars_dict[string[window_start]] -= 1

            if chars_dict[string[window_start]] == 0:
                del chars_dict[string[window_start]]

            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)

    return max_length


def main():

    print(length_of_longest_substring("aabccbb", 2))
    print(length_of_longest_substring("abbcb", 1))
    print(length_of_longest_substring("abccde", 1))


main()
