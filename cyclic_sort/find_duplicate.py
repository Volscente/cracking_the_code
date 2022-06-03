"""
We are given an unsorted array containing ‘n+1’ numbers taken from the range 1 to ‘n’.
The array has only one duplicate but it can be repeated multiple times.
Find that duplicate number without using any extra space. You are, however, allowed to modify the input array.

Example 1:
Input: [1, 4, 4, 3, 2]
Output: 4

Example 2:
Input: [2, 1, 3, 3, 5, 4]
Output: 3

Example 3:
Input: [2, 4, 1, 4, 4]
Output: 4

Time Complexity: O(N)
space Complexity: O(1)
"""


def find_duplicate(nums):
    """
    Order the array by swapping elements in their index position.
    In the moment you swap an item with the exact same item, you found the duplicate
    :param nums: List
    :return: Duplicate number
    """

    i = 0

    while i < len(nums):

        if nums[i] != i + 1:

            number_index = nums[i] - 1

            if nums[i] != nums[number_index]:

                nums[i], nums[number_index] = nums[number_index], nums[i]

            else:

                return nums[i]

        else:

            i += 1

    return -1


def main():
    print(find_duplicate([1, 4, 4, 3, 2]))
    print(find_duplicate([2, 1, 3, 3, 5, 4]))
    print(find_duplicate([2, 4, 1, 4, 4]))


main()
