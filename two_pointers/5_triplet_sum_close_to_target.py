"""
Given an array of unsorted numbers and a target number,
find a triplet in the array whose sum is as close to the target number as possible, return the sum of the triplet.
If there are more than one such triplet, return the sum of the triplet with the smallest sum.

Example 1:
Input: [-2, 0, 1, 2], target=2
Output: 1
Explanation: The triplet [-2, 1, 2] has the closest sum to the target.

Example 2:
Input: [-3, -1, 1, 2], target=1
Output: 0
Explanation: The triplet [-3, 1, 2] has the closest sum to the target.

Example 3:
Input: [1, 0, 1, 1], target=100
Output: 3
Explanation: The triplet [1, 1, 1] has the closest sum to the target.
"""

import math


def triplet_sum_close_to_target(nums, target_sum):
    """
    Time Complexity: O(N * logN + N^2) = O(N^2)
    Space Complexity: O(N) -> Required for sorting
    :param nums:
    :param target_sum:
    :return:
    """

    # O(N * logN)
    nums.sort()

    smallest_distance = math.inf

    # O(N)
    for i in range(len(nums) - 2):

        left, right = i + 1, len(nums) - 1

        # O(N)
        while left < right:

            target_difference = target_sum - nums[i] - nums[left] - nums[right]

            if target_difference == 0:
                return target_sum

            if (abs(target_difference) < abs(smallest_distance)) \
                    or ((abs(target_difference) == abs(smallest_distance)) and (target_difference > smallest_distance)):
                smallest_distance = target_difference

            if target_difference > 0:
                left += 1
            else:
                right -= 1

    return target_sum - smallest_distance


def main():
    print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))
    print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))
    print(triplet_sum_close_to_target([1, 0, 1, 1], 100))


main()
