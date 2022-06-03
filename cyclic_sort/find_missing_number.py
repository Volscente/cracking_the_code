"""
We are given an array containing n distinct numbers taken from the range 0 to n.
Since the array has only n numbers out of the total n+1 numbers, find the missing number.

Example 1:
Input: [4, 0, 3, 1]
Output: 2

Example 2:
Input: [8, 3, 5, 2, 4, 6, 0, 1]
Output: 7

Time Complexity: O(N)
Space Complexity: O(1)
"""


def find_missing_number(nums):
    i = 0
    n = len(nums)

    while i < n:
        print('iteration')
        num = nums[i]

        # Exclude the n_th number 'num < n'
        if num < n and num != nums[num]:
            nums[i], nums[num] = nums[num], nums[i]
        else:
            i += 1

    # Look for misplaced number
    for j in range(len(nums)):
        if j != nums[j]:
            return j

    # Misplace is n_th number
    return j


def main():
    print(find_missing_number([4, 0, 3, 1]))
    # print(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))


main()
