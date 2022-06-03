"""
We are given an unsorted array containing numbers taken from the range 1 to ‘n’.
The array can have duplicates, which means some numbers will be missing. Find all those missing numbers.

Example 1:
Input: [2, 3, 1, 8, 2, 3, 5, 1]
Output: 4, 6, 7
Explanation: The array should have all numbers from 1 to 8, due to duplicates 4, 6, and 7 are missing.

Example 2:
Input: [2, 4, 1, 2]
Output: 3

Example 3:
Input: [2, 3, 2, 1]
Output: 4

Time Complexity: O(N)
Space Complexity: O(1)
"""


def find_missing_numbers(nums):
    i = 0
    n = len(nums)
    missing_numbers = []

    while i < n:

        number_index = nums[i] - 1

        if nums[i] != nums[number_index]:

            nums[i], nums[number_index] = nums[number_index], nums[i]

        else:

            i += 1

    for k in range(n):
        if nums[k] != k + 1:
            missing_numbers.append(k + 1)

    return missing_numbers


def main():
    print(find_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]))
    print(find_missing_numbers([2, 4, 1, 2]))
    print(find_missing_numbers([2, 3, 2, 1]))


main()
