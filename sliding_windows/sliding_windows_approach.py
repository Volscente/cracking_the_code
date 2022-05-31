def find_averages_of_subarrays(k, arr):

    result = []

    window_sum, window_start = 0.0, 0

    for window_end in range(len(arr)):

        print('window_end: ' + str(window_end))

        window_sum += arr[window_end]  # add the next element

        print('window_sum: ' + str(window_sum))

        # slide the window, we don't need to slide if we've not hit the required window size of 'k'

        if window_end >= k - 1:
            result.append(window_sum / k)  # calculate the average
            window_sum -= arr[window_start]  # subtract the element going out
            window_start += 1  # slide the window ahead

    return result


def visualize_sliding_window(k, arr):

    print(arr)
    print('\n')
    window_start = 0

    for window_end in range(len(arr)):

        print(arr[window_start:window_end + 1])

        if window_end >= k - 1:

            window_start += 1


def main():

    arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
    k = 5

    # result = find_averages_of_subarrays(k, arr)
    # print("Averages of subarrays of size K: " + str(result))

    visualize_sliding_window(k, arr)


main()
