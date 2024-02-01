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


print(find_target_sum([1, 2, 3, 4, 6], 6)) # [1, 3]

print(remove_duplicates([2, 3, 3, 3, 6, 9, 9])) # 4

        