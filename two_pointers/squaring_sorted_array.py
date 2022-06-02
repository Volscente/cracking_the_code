"""
Given a sorted array, create a new array containing squares of all the numbers of the input array in the sorted order.

Example 1:
Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]

Example 2:
Input: [-3, -1, 0, 1, 2]
Output: [0, 1, 1, 4, 9]

Time Complexity: O(N)
Space Complexity: O(N)
"""


def make_squares(arr):
    n = len(arr)
    squares = [0 for x in range(n)]

    left = 0
    right = n - 1
    highest_square_index = n - 1

    while left <= right:

        left_square = arr[left] * arr[left]
        right_square = arr[right] * arr[right]

        if left_square > right_square:
            squares[highest_square_index] = left_square
            left += 1
        else:
            squares[highest_square_index] = right_square
            right -= 1

        highest_square_index -= 1

    return squares


def main():
    print("Squares: " + str(make_squares([-2, -1, 0, 2, 3])))
    print("Squares: " + str(make_squares([-3, -1, 0, 1, 2])))


main()
