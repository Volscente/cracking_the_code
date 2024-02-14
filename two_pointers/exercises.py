def find_target_sum(arr, target_sum):
    """
    Given an ordered array of numbers, find the indices of the two number within it that corresponds to a target sum
    """

    start, end = 0, len(arr) - 1

    while start < end:

        computed_sum = arr[start] + arr[end]

        if computed_sum == target_sum:

            return [start, end]
        
        elif computed_sum > target_sum:

            end -= 1

        else:

            start += 1

    return [-1, -1]

def remove_duplicates(arr):
    """
    Given an ordered array of numbers, remove duplicates by pushing back to the end of the array in place and return the length of the sub-sequence of non-duplicate numbers
    """

    start, end = 0, 1

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

def make_squares(arr):

    square_arr = [0 for x in range(len(arr))]

    left, right = 0, len(arr) - 1

    highest_square_index = len(arr) - 1

    while left <= right:

        square_left = arr[left] * arr[left]
        square_right = arr[right] * arr[right]

        if square_left > square_right:

            square_arr[highest_square_index] = square_left
            left += 1

        else:

            square_arr[highest_square_index] = square_right
            right -= 1

        highest_square_index -= 1

    return square_arr




print(find_target_sum([1, 2, 3, 4, 6], 6)) # [1, 3]

print(remove_duplicates([2, 3, 3, 3, 6, 9, 9])) # 4

print(make_squares([-2, -1, 0, 2, 3])) # [0, 1, 4, 4, 9]

        