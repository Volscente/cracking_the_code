def find_average_subarrays_k_length(arr, k):

    result = []

    window_sum, window_start = 0.0, 0

    for window_end in range(len(arr)):

        window_sum += arr[window_end]

        if window_end >= k - 1:

            result.append(window_sum / k)
            window_sum -= arr[window_start]
            window_start += 1

    return result

def main():

    arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
    k = 5

    print(find_average_subarrays_k_length(arr, k))


main()