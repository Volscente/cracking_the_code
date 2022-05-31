"""
Problem Statement#
You are visiting a farm to collect fruits. The farm has a single row of fruit trees. You will be given two baskets,
and your goal is to pick as many fruits as possible to be placed in the given baskets.

You will be given an array of characters where each character represents a fruit tree. The farm has following restrictions:

Each basket can have only one type of fruit. There is no limit to how many fruit a basket can hold.
You can start with any tree, but you can’t skip a tree once you have started.
You will pick exactly one fruit from every tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.
Write a function to return the maximum number of fruits in both baskets.

Example 1:
Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

Example 2:
Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket.
This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']
"""


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
This problem follows the Sliding Window pattern and is quite similar to Longest Substring with K Distinct Characters. 
In this problem, we need to find the length of the longest subarray with no more than two distinct characters (or fruit types!). 
This transforms the current problem into Longest Substring with K Distinct Characters where K=2.
['A', 'B', 'C', 'A', 'C']
3


1 - [A] {A: 1} max = 1

2- [A, B] {A: 1, B: 1} max = 2

3 - [A, B, C] {A: 1, B: 1, C: 1} -> {B: 1, C: 1} [B, C]

4 - [B, C, A] {B: 1, C: 1, A:1 } -> {C: 1, A: 1} [C, A]

5 - [C, A, C] {C: 2, A: 1}

"""
