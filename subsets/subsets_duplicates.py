"""
Given a set of numbers that might contain duplicates, find all of its distinct subsets.

Example 1:
Input: [1, 3, 3]
Output: [], [1], [3], [1,3], [3,3], [1,3,3]

Example 2:
Input: [1, 5, 3, 3]
Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3], [3,3], [1,3,3], [3,3,5], [1,5,3,3]

Time Complexity: O(N) fetch numbers O(2^N) fetch the subsets (since they double) -> O(N * 2^N)
Space Complexity: O(N * 2^N) -> nums dimension per subsets dimension
"""


def find_subsets(nums):

    subsets =[[]]

    start_index, end_index = 0, 0

    for i in range(len(nums)):

        start_index = 0

        if i > 0 and nums[i] == nums[i - 1]:

            start_index = end_index + 1

        end_index = len(subsets)

        for j in range(start_index, end_index):

            new_set = list(subsets[j])
            new_set.append(nums[i])
            subsets.append(new_set)

    return subsets


def main():

    print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))


main()
