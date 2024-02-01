def find_target_sum(arr, target_sum):
    """
    Given an ordered array of numbers, find the indices of the two number within it that corresponds to a target sum
    """

    left, right = 0, len(arr) - 1

    while (left < right):

        computed_sum = arr[left] + arr[right]

        if computed_sum == target_sum:

            return [left, right]
        
        elif target_sum > computed_sum:

            left += 1

        else:

            right -= 1

    return [-1, -1]


print(find_target_sum([1, 2, 3, 4, 6], 6)) # [1, 3]

        