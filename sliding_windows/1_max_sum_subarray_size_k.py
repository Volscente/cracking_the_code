"""
Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.

Example 1
Input: [2, 1, 5, 1, 3, 2], k=3
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].

Example 2
Input: [2, 3, 4, 1, 5], k=2
Output: 7
Explanation: Subarray with maximum sum is [3, 4].

Time Complexity: O(N) -> All the N elements of the array have to be looped
Space Complexity: O(1)
"""


def max_sub_array_of_size_k(k, arr):
    max_value = 0
    max_sequence = []

    window_start = 0
    window_sum = 0

    for window_end in range(len(arr)):

        window_sum += arr[window_end]

        if window_end >= k - 1:

            if window_sum > max_value:
                max_value = window_sum
                max_sequence = arr[window_start:window_end + 1]

            window_sum -= arr[window_start]
            window_start += 1

    return max_value


def main():

    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))


main()
