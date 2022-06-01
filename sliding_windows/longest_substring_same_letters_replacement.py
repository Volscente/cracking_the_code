def length_of_longest_substring(string, k):

    """
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
