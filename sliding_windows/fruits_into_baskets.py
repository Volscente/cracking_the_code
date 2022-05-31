def fruits_into_baskets(fruits):
    """
    Time Complexity: O(N)
    Space Complexity: O(K)
    :param fruits:
    :return:
    """
    baskets = {}
    max_fruits = 0

    window = []
    window_start = 0

    for window_end in range(len(fruits)):

        window += fruits[window_end]

        if fruits[window_end] in baskets.keys():

            baskets[fruits[window_end]] += 1

        else:

            baskets[fruits[window_end]] = 1

        if len(baskets.keys()) <= 2:

            max_fruits = max(max_fruits, len(window))

        else:

            baskets[fruits[window_start]] -= 1

            if baskets[fruits[window_start]] == 0:
                del baskets[fruits[window_start]]

            window.pop(0)
            window_start += 1

        print(baskets)

    return max_fruits


def main():
    print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
    print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))


main()

"""
['A', 'B', 'C', 'A', 'C']
3


1 - [A] {A: 1} max = 1

2- [A, B] {A: 1, B: 1} max = 2

3 - [A, B, C] {A: 1, B: 1, C: 1} -> {B: 1, C: 1} [B, C]

4 - [B, C, A] {B: 1, C: 1, A:1 } -> {C: 1, A: 1} [C, A]

5 - [C, A, C] {C: 2, A: 1}

"""
