"""
Given an array of numbers sorted in ascending order, find the range of a given number ‘key’.
The range of the ‘key’ will be the first and last position of the ‘key’ in the array.

Write a function to return the range of the ‘key’. If the ‘key’ is not present return [-1, -1].

Example 1:
Input: [4, 6, 6, 6, 9], key = 6
Output: [1, 3]

Example 2:
Input: [1, 3, 8, 10, 15], key = 10
Output: [3, 3]

Example 3:
Input: [1, 3, 8, 10, 15], key = 12
Output: [-1, -1]

Time Complexity: O(logN)
Space Complexity: O(1)
"""


def find_range(arr, key):
    start, end = 0, len(arr) - 1

    if key > arr[end] or key < arr[start]:
        return [-1, -1]

    while start <= end:

        middle = start + (end - start) // 2

        if key < arr[middle]:
            end = middle - 1
        elif key > arr[middle]:
            start = middle + 1
        else:

            left, right = middle, middle

            while arr[left] == key:
                left -= 1
            while arr[right] == key:
                right += 1

            return [left + 1, right - 1]

    result = [- 1, -1]
    return result


def main():
    print(find_range([4, 6, 6, 6, 9], 6))
    print(find_range([1, 3, 8, 10, 15], 10))
    print(find_range([1, 3, 8, 10, 15], 12))


main()
