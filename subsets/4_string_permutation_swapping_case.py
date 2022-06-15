"""
Given a string, find all of its permutations preserving the character sequence but changing case.

Example 1:

Input: "ad52"
Output: "ad52", "Ad52", "aD52", "AD52"
Example 2:

Input: "ab7c"
Output: "ab7c", "Ab7c", "aB7c", "AB7c", "ab7C", "Ab7C", "aB7C", "AB7C"
"""


def string_case_permutation(string):
    """
    Time complexity: O(N * 2^N)
    Space Complexity: O(N * 2^N)
    :param string:
    :return:
    """

    permutations = [string]

    # O(N)
    for i in range(len(string)):

        if string[i].isalpha():

            # O(2^N)
            for j in range(len(permutations)):

                new_permutation = list(permutations[j])
                new_permutation[i] = new_permutation[i].swapcase()
                permutations.append(''.join(new_permutation))

    return permutations


def main():

    print(string_case_permutation('ad52'))
    print(string_case_permutation('ab7c'))


main()
