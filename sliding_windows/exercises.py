def compute_avg_subarrays(arr, k):

    window_sum = 0.0
    window_start = 0
    results = []

    for window_end in range(len(arr)):

        window_sum += arr[window_end]

        if window_end >= k - 1:

            results.append(window_sum / k)
            window_sum -= arr[window_start]
            window_start += 1

    return results

def max_sub_array_of_size_k(arr, k):

    window_start = 0
    window_sum = 0
    max_sum = 0

    for window_end in range(len(arr)):

        window_sum += arr[window_end]

        if window_end >= k - 1:

            if window_sum >= max_sum:

                max_sum = window_sum

            window_sum -= arr[window_start]
            window_start += 1

    return max_sum



print(compute_avg_subarrays([1, 3, 3, 5], 2)) # Output: [2, 3, 4]

print(max_sub_array_of_size_k([2, 1, 5, 1, 3, 2], 3)) # Output: 9