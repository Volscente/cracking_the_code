import math


def smallest_subarray_sum(s, arr):
    """
    Time Complexity: O(N^2)
    Space Complexity: O(1)
    :param s: number
    :param arr: array
    :return: Integer
    """
    for k in range(1, len(arr) + 1):

        window_start = 0
        window_sum = 0

        for window_end in range(len(arr)):

            window_sum += arr[window_end]

            if window_end >= k - 1:

                if window_sum >= s:
                    return (window_end - window_start) + 1

                window_sum -= arr[window_start]
                window_start += 1

    return 0


def smallest_subarray_sum_improved(s, arr):
    """
    Time Complexity: O(N)
    Space Complexity: O(1)
    :param s:
    :param arr:
    :return:
    """

    min_length = math.inf
    window_start = 0
    window_sum = 0

    for window_end in range(len(arr)):

        window_sum += arr[window_end]

        while window_sum >= s:

            min_length = min(min_length, window_end-window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1

    if min_length == math.inf:

        return 0

    else:

        return min_length


def main():
    print("Smallest subarray length: " + str(smallest_subarray_sum_improved(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: " + str(smallest_subarray_sum_improved(8, [3, 4, 1, 1, 6])))
    print("Smallest subarray length: " + str(smallest_subarray_sum_improved(8, [2, 1, 5, 2, 3, 2])))


main()
