"""
In a non-empty array of integers, every number appears twice except for one, find that single number.

Example 1:
Input: 1, 4, 2, 1, 3, 2, 3
Output: 4

Example 2:
Input: 7, 9, 7
Output: 9


Solution:
Recall the following two properties of XOR:

It returns zero if we take XOR of two same numbers.
It returns the same number if we XOR with zero.

So we can XOR all the numbers in the input;
duplicate numbers will zero out each other and we will be left with the single number

Time Complexity: O(N)
Space Complexity: O(1)
"""


def single_number(arr):

    # Start from 0 to make: arr[0] XOR arr[1]
    # Because 0 XOR num = num
    x1 = 0

    for num in arr:

        # XOR each number with the following one
        x1 = x1 ^ num

        print(num)
        print(x1)
        print('\n')

    return x1


def main():

    arr = [1, 2, 3, 2, 3]
    print(single_number(arr))


main()

