"""
Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

Example 1:
Input: [-3, 0, 1, 2, -1, 1, -2]
Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
Explanation: There are four unique triplets whose sum is equal to zero.

Example 2:
Input: [-5, 2, -1, -2, 3]
Output: [[-5, 2, 3], [-2, -1, 3]]
Explanation: There are two unique triplets whose sum is equal to zero.

Solution:
This problem follows the Two Pointers pattern and shares similarities with Pair with Target Sum.
A couple of differences are that the input array is not sorted and instead of a pair we need to find triplets with a
target sum of zero.

To follow a similar approach, first, we will sort the array and then iterate through it taking one number at a time.
Let’s say during our iteration we are at number ‘X’, so we need to find ‘Y’ and ‘Z’ such that X + Y + Z == 0.
At this stage, our problem translates into finding a pair whose sum is equal to “-X” (as from the above equation Y + Z == -X).

Another difference from Pair with Target Sum is that we need to find all the unique triplets.
To handle this, we have to skip any duplicate number. Since we will be sorting the array,
so all the duplicate numbers will be next to each other and are easier to skip.
"""


def search_triplets(arr):
    """
    Time Complexity: O(N*logN) + O(N^2) -> O(N^2)
    Space Complexity: O(N)
    :param arr:
    :return:
    """

    triplets = []

    # O(N*logN)
    arr.sort()

    # O(N)
    for i in range(len(arr)):

        if i > 0 and arr[i] == arr[i -1]:
            continue

        # O(N)
        search_pair_target_sum(arr, -arr[i], i+1, triplets)

    return triplets


def search_pair_target_sum(arr, target_sum, left, triplets):

    right = len(arr) - 1

    # O(N)
    while left < right:

        computed_sum = arr[left] + arr[right]

        if target_sum == computed_sum:

            triplets.append([-target_sum, arr[left], arr[right]])
            left += 1
            right -= 1

            # 1 1 0 4 5 5 -> left 1 right 5 -> left 1 right 5

            while left < right and arr[left] == arr[left - 1]:
                left += 1
            while left < right and arr[right] == arr[right + 1]:
                right -= 1

        elif target_sum > computed_sum:
            left += 1
        else:
            right -= 1


"""
4 -1 -2 0 4 -1 -5 1 1

-5 -2 -1 -1 0 1 1 4 4

arr[i] -> -5
left -2 right 4 -> 2 ... left -1 right 4 -> 3 -> -1 4 = 3 -> 0 4 = 4 -> 1 4 = 5 [-5, 1, 4] -> 1 4

arr[i] -2 [-5, 1, 4]
l -1 r 4 = 3 -> l -1 r 4 = 3 -> l -1 r 1 -> l -1 r 1 = 0
l 0 r 1 = 1
l 1 r 1 = 2 [[-5, 1, 4], [-2, 1, 1]]

arr[i] -1
-1 4 = 3
-1 4 = 3
-1 1 = 0
0 1 = 1 [[-5, 1, 4], [-2, 1, 1], [-1, 0, 1]]

arr[i] -1 -> 1
0 4 = 4
0 4 = 4
0 1 = 1 [[-5, 1, 4], [-2, 1, 1], [-1, 0, 1], [-1, 0, 1]

arr[i] 0 
"""

