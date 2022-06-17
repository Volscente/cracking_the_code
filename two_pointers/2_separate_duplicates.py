"""
Given an array of sorted numbers, separate all duplicates from it in-place. You should not use any extra space;
move all duplicates at the end of the array and after moving return the length of the subarray that has no duplicate in it.

Example 1:
Input: [2, 3, 3, 3, 6, 9, 9]
Output: 4
Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].

Example 2:
Input: [2, 2, 2, 11]
Output: 2
Explanation: The first two elements after removing the duplicates will be [2, 11].
"""


def remove_duplicates(arr):
    start = 0
    end = 1

    for i in range(len(arr)):

        if arr[start] > arr[end]:
            return len(arr[:start + 1])

        if arr[start] == arr[end]:

            duplicated = arr.pop(end)
            arr.append(duplicated)

        else:

            start += 1
            end += 1

    return len(arr[:start + 1])


def remove_duplicates_improved(arr):
    """
    Time Complexity: O(N)
    Space Complexity: O(1)
    :param arr:
    :return:
    """
    i = 0
    next_non_duplicate = 1

    while i < len(arr):

        if arr[next_non_duplicate - 1] != arr[i]:
            arr[next_non_duplicate] = arr[i]
            next_non_duplicate += 1
        i += 1

    return next_non_duplicate


def main():
    print(remove_duplicates_improved([2, 3, 3, 3, 6, 9, 9]))
    print(remove_duplicates_improved([2, 2, 2, 11]))


main()
